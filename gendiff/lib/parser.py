import os.path
import json

import yaml


def parse(file_path):
    (name, extension) = os.path.splitext(file_path)
    if extension == ".json":
        return json.load(open(file_path))
    elif extension == ".yaml" or extension == ".yml":
        return yaml.safe_load(open(file_path))
