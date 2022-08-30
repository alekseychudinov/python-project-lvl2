import json
import os.path

import yaml


def parse(file, format_name):
    if format_name == "JSON":
        return json.load(file)
    elif format_name == "YAML":
        return yaml.safe_load(file)


def get_data(file_path):
    extension = os.path.splitext(file_path)[1]
    file = open(file_path)
    if extension == ".json":
        return parse(file, "JSON")
    elif extension == ".yaml" or extension == ".yml":
        return parse(file, "YAML")
    else:
        return "Неизвестный формат предоставленных данных"
