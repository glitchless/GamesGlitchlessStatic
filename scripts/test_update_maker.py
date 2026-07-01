import json, os, tempfile, importlib.util, hashlib

spec = importlib.util.spec_from_file_location(
    "um", os.path.join(os.path.dirname(__file__), "update-maker.py"))
um = importlib.util.module_from_spec(spec); spec.loader.exec_module(um)


def _read(path):
    with open(path) as f:
        return json.load(f)


def test_v1_stays_pure_buckets_and_v2_has_sha256():
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "incremental", "p"); os.makedirs(src)
        with open(os.path.join(src, "a.txt"), "w") as f: f.write("hello")
        idx = os.path.join(d, "incremental", "indexes", "p.json")
        os.makedirs(os.path.dirname(idx))
        clog = os.path.join(d, "incremental", "p_changelog.json")
        clog2 = os.path.join(d, "incremental", "p_changelogv2.json")
        cwd = os.getcwd(); os.chdir(d)
        try:
            um.make_changelog("incremental/p", idx, clog)
        finally:
            os.chdir(cwd)
        # v1 untouched: buckets only, NO sha256
        v1 = _read(clog)
        assert "sha256" not in v1, v1
        ts = [k for k in v1 if k.isdigit()]
        assert ts and v1[ts[0]]["/a.txt"] == 1, v1
        # v2 is a new file: same bucket + full sha256 map
        v2 = _read(clog2)
        assert v2[ts[0]]["/a.txt"] == 1, v2
        assert v2["sha256"]["/a.txt"] == hashlib.sha256(b"hello").hexdigest(), v2
        # md5 index unchanged in form (hex md5)
        assert _read(idx)["incremental/p/a.txt"] == hashlib.md5(b"hello").hexdigest()


def test_v2_full_state_prunes_removed_file():
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "incremental", "p"); os.makedirs(src)
        with open(os.path.join(src, "a.txt"), "w") as f: f.write("hello")
        idx = os.path.join(d, "incremental", "indexes", "p.json")
        os.makedirs(os.path.dirname(idx))
        clog = os.path.join(d, "incremental", "p_changelog.json")
        clog2 = os.path.join(d, "incremental", "p_changelogv2.json")
        cwd = os.getcwd(); os.chdir(d)
        try:
            um.make_changelog("incremental/p", idx, clog)
            os.remove(os.path.join("incremental", "p", "a.txt"))
            with open(os.path.join("incremental", "p", "b.txt"), "w") as f: f.write("world")
            um.make_changelog("incremental/p", idx, clog)
        finally:
            os.chdir(cwd)
        v2 = _read(clog2)
        assert "/a.txt" not in v2["sha256"], v2["sha256"]
        assert v2["sha256"]["/b.txt"] == hashlib.sha256(b"world").hexdigest()
        # v1 stays pure buckets and records the removal as 0
        v1 = _read(clog)
        assert "sha256" not in v1, v1
        assert any(v.get("/a.txt") == 0 for k, v in v1.items() if k.isdigit()), v1


def test_v2_backfilled_on_empty_diff_when_missing():
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "incremental", "p"); os.makedirs(src)
        with open(os.path.join(src, "a.txt"), "w") as f: f.write("hello")
        with open(os.path.join(src, "c.txt"), "w") as f: f.write("cee")
        idx = os.path.join(d, "incremental", "indexes", "p.json")
        os.makedirs(os.path.dirname(idx))
        clog = os.path.join(d, "incremental", "p_changelog.json")
        clog2 = os.path.join(d, "incremental", "p_changelogv2.json")
        cwd = os.getcwd(); os.chdir(d)
        try:
            um.make_changelog("incremental/p", idx, clog)   # creates v1 + v2
            os.remove(clog2)                                 # simulate v2 not generated yet
            um.make_changelog("incremental/p", idx, clog)   # empty diff -> v2 must be (re)created
        finally:
            os.chdir(cwd)
        # Full current-state map: every current file present, even though the diff was empty.
        v2 = _read(clog2)
        assert v2["sha256"]["/a.txt"] == hashlib.sha256(b"hello").hexdigest(), v2
        assert v2["sha256"]["/c.txt"] == hashlib.sha256(b"cee").hexdigest(), v2


if __name__ == "__main__":
    test_v1_stays_pure_buckets_and_v2_has_sha256()
    test_v2_full_state_prunes_removed_file()
    test_v2_backfilled_on_empty_diff_when_missing()
    print("OK")
