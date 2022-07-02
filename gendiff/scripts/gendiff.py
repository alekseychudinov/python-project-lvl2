#!/usr/bin/env python
from gendiff.lib.cli import parse_args
from gendiff.lib.formatter import formatting
from gendiff.lib.parser import parse


def main():
    file_path1, file_path2, format_name = parse(parse_args())
    diff = generate_diff(file_path1, file_path2)
    result = formatting(diff, format_name)
    print(result)


def generate_diff(ile_path1, file_path2):
    return {"type": "root", "children": make_children(ile_path1, file_path2)}


def make_children(data1, data2):
    result = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data2:
            result.append({"key": key, "type": "deleted", "value": data1[key]})
        elif key not in data1:
            result.append({"key": key, "type": "added", "value": data2[key]})
        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append(
                    {
                        "key": key,
                        "type": "parent",
                        "children": make_children(data1[key], data2[key]),
                    }
                )
            elif data1[key] == data2[key]:
                result.append({"key": key, "type": "unchanged", "value": data1[key]})
            else:
                result.append(
                    {
                        "key": key,
                        "type": "updated",
                        "value1": data1[key],
                        "value2": data2[key],
                    }
                )
    return result


if __name__ == "__main__":
    main()
