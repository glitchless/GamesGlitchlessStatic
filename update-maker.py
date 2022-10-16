#!/usr/bin/env python3

import hashlib
import os
import traceback
import json
import time


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def checksum_file(path):
    with open(path, mode='rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def make_index(dir_path):
    result = {}

    for root, dirs, files in os.walk(dir_path):
        for name in files:
            path = os.path.join(root, name)
            result[path] = checksum_file(path)

    return result


def load_index(path):
    try:
        with open(path, mode='r') as f:
            return json.load(f)
    except:
        return {}


def save_index(index, path):
    with open(path, mode='w') as f:
        json.dump(index, f, sort_keys=True, ensure_ascii=False, indent=4)


def diff_index(index1, index2):
    result = {path: None for path in set(index1.keys()) | set(index2.keys())}

    for path, checksum in index2.items():
        if path not in index1 or checksum != index1[path]:
            result[path] = 1

    for path, checksum in index1.items():
        if path not in index2:
            result[path] = 0

    result = {k: v for k, v in result.items() if v is not None}

    return result


def add_diff_to_changelog(changelog, diff):
    changelog[str(int(time.time()))] = diff


def print_diff(diff):
    print('NEW DIFF:')
    print(json.dumps(diff, sort_keys=True, ensure_ascii=False, indent=4))


def add_prefix_in_values(values, base_path):
    new_values = {}
    for key, value in values.items():
        absolute_path = os.path.join(base_path, key)
        new_values[absolute_path] = value

    return new_values


def load_changelog(base_path, path):
    load_json = {}
    try:
        with open(path, mode='r') as f:
            load_json = json.load(f)
    except:
        return {}
    return_json = {}

    for key, values in load_json.items():
        return_json[key] = add_prefix_in_values(values, base_path)

    return return_json


def remove_prefix_in_values(values, base_path):
    new_values = {}
    for key, value in values.items():
        relative_path = remove_prefix(key, base_path)
        new_values[relative_path] = value

    return new_values


def save_changelog(base_path, changelog, path):
    to_save = {}

    for key, values in changelog.items():
        to_save[key] = remove_prefix_in_values(values, base_path)

    with open(path, mode='w') as f:
        json.dump(to_save, f, sort_keys=True, ensure_ascii=False, indent=4)


def make_changelog(source_dir_path, output_index_path, output_changelog_path):
    old_index = load_index(output_index_path)
    new_index = make_index(source_dir_path)
    diff = diff_index(old_index, new_index)
    changelog = load_changelog(source_dir_path, output_changelog_path)
    add_diff_to_changelog(changelog, diff)

    print_diff(diff)

    if len(diff) != 0:
        save_index(new_index, output_index_path)
        save_changelog(source_dir_path, changelog, output_changelog_path)


def run_with_arguments():
    try:
        source_dir_path = os.sys.argv[1]
        output_index_path = os.sys.argv[2]
        output_changelog_path = os.sys.argv[3]

        make_changelog(source_dir_path, output_index_path, output_changelog_path)
    except ValueError:
        traceback.print_exc()
        print('USAGE: python3 update-maker.py SOURCE_DIR OUTPUT_INDEX OUTPUT_CHANGELOG')
        exit(1)


def main():
    if len(os.sys.argv) > 1:
        run_with_arguments()
        return

    packs = ['gtnh', 'vanilla', 'asworkaround']
    for name in packs:
        make_changelog('incremental/' + name,
                       'incremental/indexes/' + name + '.json',
                       'incremental/' + name + '_changelog.json')


if __name__ == '__main__':
    main()
