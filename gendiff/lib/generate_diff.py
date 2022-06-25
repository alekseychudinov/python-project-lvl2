import json
import os.path

import yaml
from gendiff.lib.build_diff import build_diff
from gendiff.format_package.stylish import stylish
from gendiff.format_package.plain import plain


def generate_diff(file_path1, file_path2, format_name='json'):
    (name1, extension1) = os.path.splitext(file_path1)
    (name2, extension2) = os.path.splitext(file_path2)
    if (extension1 == ".json") and (extension2 == ".json"):
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
    elif (extension1 == ".yaml" and extension2 == ".yaml") or (
        extension1 == ".yml" and extension2 == ".yml"
    ):
        file1 = yaml.safe_load(open(file_path1))
        file2 = yaml.safe_load(open(file_path2))
    else:
        return "Файл не найден"
    result_dict = build_diff(file1, file2)
    # print(result_dict, 'result_dict')
    result_str = ''
    if format_name == "json":
        result_str = stylish(result_dict)
    elif format_name == "plain":
        result_str = plain(result_dict)
    # print(result_str, 'result_str')
    return result_str
