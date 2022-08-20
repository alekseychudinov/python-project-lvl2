import json


def json_format(diff_dict):
    return json.dumps(diff_dict, indent=4)
