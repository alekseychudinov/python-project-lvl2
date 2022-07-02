def json_format(diff_dict):
    string = "{\n"
    string += "    " + '"type":' + ' "' + diff_dict["type"] + '",\n'
    string += "    " + '"children": [' + "\n"
    string = make_sub_string(diff_dict["children"], string, 2) + "]"
    string += "\n}"
    return string


def make_sub_string(sub_list, sub_string, depth):
    for index, item_dict in enumerate(sub_list):
        if "children" in item_dict:
            sub_string += "    " * (depth - 1) + "{\n"
            sub_string += "    " * depth + '"key":' + ' "' + item_dict["key"] + '",\n'
            sub_string += "    " * depth + '"type":' + ' "' + item_dict["type"] + '",\n'
            sub_string += "    " * depth + '"children": [' + "\n"
            sub_string = (
                make_sub_string(item_dict["children"], sub_string, depth + 1) + "]\n"
            )
            sub_string += "    " * (depth - 1) + "}"
        elif item_dict["type"] != "updated":
            sub_string += "    " * (depth - 1) + "{" + "\n"
            sub_string += "    " * depth + '"key":' + ' "' + item_dict["key"] + '",\n'
            sub_string += "    " * depth + '"type":' + ' "' + item_dict["type"] + '",\n'
            sub_string += (
                "    " * depth
                + '"value": '
                + map_value(item_dict["value"], depth)
                + "\n"
            )
            sub_string += "    " * (depth - 1) + "}"
        elif item_dict["type"] == "updated":
            sub_string += "    " * (depth - 1) + "{" + "\n"
            sub_string += "    " * depth + '"key":' + ' "' + item_dict["key"] + '",\n'
            sub_string += "    " * depth + '"type":' + ' "' + item_dict["type"] + '",\n'
            sub_string += (
                "    " * depth
                + '"value1": '
                + map_value(item_dict["value1"], depth)
                + ",\n"
            )
            sub_string += (
                "    " * depth
                + '"value2": '
                + map_value(item_dict["value2"], depth)
                + "\n"
            )
            sub_string += "    " * (depth - 1) + "}"
        if index < len(sub_list) - 1:
            sub_string += ",\n"
    return sub_string


def map_value(key_value, depth):
    if isinstance(key_value, dict):
        return (
            map_dict_value(key_value, "\n" + "    " * depth + "{\n", depth + 1)
            + "    " * depth
            + "}"
        )
    elif str(key_value) == "True":
        return "true"
    elif str(key_value) == "False":
        return "false"
    elif str(key_value) == "None":
        return "null"
    elif isinstance(key_value, int):
        return str(key_value)
    else:
        return '"' + str(key_value) + '"'


def map_dict_value(value_dict, sub_string, any_depth):
    for i, key in enumerate(value_dict):
        if isinstance(value_dict[key], dict):
            sub_string += "    " * any_depth + '"' + key + '"' + ": \n"
            sub_string += "    " * any_depth + "{\n"
            sub_string = (
                map_dict_value(value_dict[key], sub_string, any_depth + 1)
                + "    " * any_depth
                + "}"
            )
        else:
            sub_string += (
                "    " * any_depth
                + '"'
                + key
                + '"'
                + ": "
                + map_value(value_dict[key], any_depth)
                + ""
            )
        if i < len(value_dict) - 1:
            sub_string += ","
        sub_string += "\n"
    return sub_string
