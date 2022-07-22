import json
import os.path

import yaml


def parse(file, extension):
    if extension == ".json":
        return json.load(file)
    elif extension == ".yaml" or extension == ".yml":
        return yaml.safe_load(file)


def get_data(file_path):
    (name, extension) = os.path.splitext(file_path)
    file = open(file_path)
    return parse(file, extension)
