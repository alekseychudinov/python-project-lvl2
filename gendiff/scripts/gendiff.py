#!/usr/bin/env python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", type=str, help="set format of output") # noqa
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    result_dict = file1 | file2
    sorted_tuple = sorted(result_dict.items(), key=lambda x: x[0])
    result_dict = dict(sorted_tuple)
    for key in result_dict:
        if key in file2 and key in file1:
            result_dict[key] = [file1[key], file2[key]]
        elif key in file1:
            result_dict[key] = [file1[key], None]
        elif key in file2:
            result_dict[key] = [None, file2[key]]
    result_str = "{\n"
    for key in result_dict:
        if result_dict[key][0] == result_dict[key][1]:
            result_str += "    " + key + ": " + result_dict[key][1] + "\n"
        elif not result_dict[key][1]:
            result_str += "  - " + key + ": " + str(result_dict[key][0]) + "\n"
        elif not result_dict[key][0]:
            result_str += "  + " + key + ": " + str(result_dict[key][1]) + "\n"
        else:
            result_str += "  - " + key + ": " + str(result_dict[key][0]) + "\n"
            result_str += "  + " + key + ": " + str(result_dict[key][1]) + "\n"
    result_str += "}"
    return result_str


if __name__ == "__main__":
    main()
