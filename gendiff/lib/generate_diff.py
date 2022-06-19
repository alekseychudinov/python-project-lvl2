import json
import yaml
import os.path


def generate_diff(file_path1, file_path2):
    (name1, extension1) = os.path.splitext(file_path1)
    (name2, extension2) = os.path.splitext(file_path2)
    file1 = {}
    file2 = {}
    if (extension1 == '.json') and (extension2 == '.json'):
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
    elif (extension1 == '.yaml' and extension2 == '.yaml') or (extension1 == '.yml' and extension2 == '.yml'):
        file1 = yaml.safe_load(open(file_path1))
        file2 = yaml.safe_load(open(file_path2))
    else:
        return 'Файл не найден'
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
