import json
import os.path

import yaml


def parse(file_path1, file_path2):
    (name1, extension1) = os.path.splitext(file_path1)
    (name2, extension2) = os.path.splitext(file_path2)
    if (extension1 == ".json") and (extension2 == ".json"):
        return (json.load(open(file_path1)), json.load(open(file_path2)))
    elif (extension1 == ".yaml" and extension2 == ".yaml") or (
        extension1 == ".yml" and extension2 == ".yml"
    ):
        return (yaml.safe_load(open(file_path1)), yaml.safe_load(open(file_path2)))
