def plain(diff_dict):
    result = make_sub_string(diff_dict["children"], "", "")
    result = result.rstrip(result[-1])
    return result


def make_sub_string(sub_list, sub_string, path_name):
    for item_dict in sub_list:
        prefix = f"Property '{path_name}{item_dict['key']}'"
        if item_dict["type"] == "added":
            sub_string = f"{sub_string}{prefix} was added with value: {map_value(item_dict['value'])}\n"
        elif item_dict["type"] == "deleted":
            sub_string = f"{sub_string}{prefix} was removed\n"
        elif item_dict["type"] == "updated":
            sub_string = (
                f"{sub_string}{prefix} was updated. From "
                f'{map_value(item_dict["value1"])} to {map_value(item_dict["value2"])}\n'
            )
        elif "children" in item_dict:
            sub_string = make_sub_string(
                item_dict["children"], sub_string, path_name + item_dict["key"] + "."
            )
    return sub_string


def map_value(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif str(key_value) == "True":
        return "true"
    elif str(key_value) == "False":
        return "false"
    elif str(key_value) == "None":
        return "null"
    elif isinstance(key_value, int):
        return str(key_value)
    else:
        return f"'{str(key_value)}'"
