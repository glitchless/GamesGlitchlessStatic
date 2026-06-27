import json, os, tempfile, importlib.util, hashlib

spec = importlib.util.spec_from_file_location(
    "um", os.path.join(os.path.dirname(__file__), "update-maker.py"))
um = importlib.util.module_from_spec(spec); spec.loader.exec_module(um)

def test_changelog_has_sha256_for_added_files_and_buckets_stay_int():
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "incremental", "p"); os.makedirs(src)
        with open(os.path.join(src, "a.txt"), "w") as f: f.write("hello")
        idx = os.path.join(d, "incremental", "indexes", "p.json")
        os.makedirs(os.path.dirname(idx))
        clog = os.path.join(d, "incremental", "p_changelog.json")
        cwd = os.getcwd(); os.chdir(d)
        try:
            um.make_changelog("incremental/p", idx, clog)
        finally:
            os.chdir(cwd)
        data = json.load(open(clog))
        # buckets are still {path: 0|1} ints
        ts_keys = [k for k in data if k.isdigit()]
        assert ts_keys, data
        assert data[ts_keys[0]]["/a.txt"] == 1
        # optional sha256 map carries the file's SHA-256
        assert "sha256" in data
        assert data["sha256"]["/a.txt"] == hashlib.sha256(b"hello").hexdigest()
        # md5 index unchanged in form (hex md5)
        index = json.load(open(idx))
        assert index["incremental/p/a.txt"] == hashlib.md5(b"hello").hexdigest()

def test_second_run_prunes_removed_and_accumulates():
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "incremental", "p"); os.makedirs(src)
        with open(os.path.join(src, "a.txt"), "w") as f: f.write("hello")
        idx = os.path.join(d, "incremental", "indexes", "p.json")
        os.makedirs(os.path.dirname(idx))
        clog = os.path.join(d, "incremental", "p_changelog.json")
        cwd = os.getcwd(); os.chdir(d)
        try:
            um.make_changelog("incremental/p", idx, clog)        # run 1: add a.txt
            os.remove(os.path.join("incremental", "p", "a.txt"))
            with open(os.path.join("incremental", "p", "b.txt"), "w") as f: f.write("world")
            um.make_changelog("incremental/p", idx, clog)        # run 2: remove a, add b
        finally:
            os.chdir(cwd)
        with open(clog) as f:
            data = json.load(f)
        assert "/a.txt" not in data["sha256"], data["sha256"]
        assert data["sha256"]["/b.txt"] == hashlib.sha256(b"world").hexdigest()
        assert any(v.get("/a.txt") == 0 for k, v in data.items() if k.isdigit()), data

if __name__ == "__main__":
    test_changelog_has_sha256_for_added_files_and_buckets_stay_int()
    test_second_run_prunes_removed_and_accumulates()
    print("OK")
