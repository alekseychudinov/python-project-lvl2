from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def formatting(result_dict, format_name):
    if format_name == "stylish":
        return stylish(result_dict)
    elif format_name == "plain":
        return plain(result_dict)
    elif format_name == "json":
        return json_format(result_dict)
