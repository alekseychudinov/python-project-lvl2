import json
import os.path

import yaml


def parse(args):
    file_path1 = args.first_file
    file_path2 = args.second_file
    format_name = args.format
    (name1, extension1) = os.path.splitext(file_path1)
    (name2, extension2) = os.path.splitext(file_path2)
    if (extension1 == ".json") and (extension2 == ".json"):
        return json.load(open(file_path1)), json.load(open(file_path2)), format_name
    elif (extension1 == ".yaml" and extension2 == ".yaml") or (
            extension1 == ".yml" and extension2 == ".yml"
    ):
        return yaml.safe_load(open(file_path1)), yaml.safe_load(open(file_path2)), format_name
