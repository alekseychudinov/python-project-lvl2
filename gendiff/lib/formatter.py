from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def formatting(result_dict, format_name):
    result_str = ""
    if format_name == "stylish":
        result_str = stylish(result_dict)
    elif format_name == "plain":
        result_str = plain(result_dict)
    elif format_name == "json":
        result_str = json_format(result_dict)
    return result_str
