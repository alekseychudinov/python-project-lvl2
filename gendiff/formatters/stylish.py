def stylish(diff_dict):
    result = make_sub_string(diff_dict["children"], "{\n", 1) + "}"
    return result


def make_sub_string(sub_list, sub_string, depth):
    for item_dict in sub_list:
        if "children" in item_dict:
            sub_string += "    " * depth + item_dict["key"] + ": {\n"
            sub_string = (
                make_sub_string(item_dict["children"], sub_string, depth + 1)
                + "    " * depth
                + "}\n"
            )
        elif item_dict["type"] == "added":
            sub_string = (
                f"{sub_string}{'    ' * (depth - 1)}  + {item_dict['key']}: "
                f"{map_value(item_dict['value'], depth)}\n"
            )
        elif item_dict["type"] == "deleted":
            sub_string = (
                f"{sub_string}{'    ' * (depth - 1)}  - {item_dict['key']}: "
                f"{map_value(item_dict['value'], depth)}\n"
            )
        elif item_dict["type"] == "unchanged":
            sub_string = (
                f"{sub_string}{'    ' * (depth - 1)}    {item_dict['key']}: "
                f"{map_value(item_dict['value'], depth)}\n"
            )
        elif item_dict["type"] == "updated":
            sub_string = (
                f"{sub_string}{'    ' * (depth - 1)}  - {item_dict['key']}: "
                f"{map_value(item_dict['value1'], depth)}\n"
            )
            sub_string = (
                f"{sub_string}{'    ' * (depth - 1)}  + {item_dict['key']}: "
                f"{map_value(item_dict['value2'], depth)}\n"
            )
    return sub_string


def map_value(key_value, depth):
    if isinstance(key_value, dict):
        return map_dict_value(key_value, "{\n", depth + 1) + "    " * depth + "}"
    elif str(key_value) == "True":
        return "true"
    elif str(key_value) == "False":
        return "false"
    elif str(key_value) == "None":
        return "null"
    else:
        return str(key_value)


def map_dict_value(value, sub_string, any_depth):
    if isinstance(value, dict):
        for key in value:
            if isinstance(value[key], dict):
                sub_string = f"{sub_string}{'    ' * any_depth}{key}: {{\n"
                sub_string = f"{map_dict_value(value[key], sub_string, any_depth + 1)}{'    ' * any_depth}}}\n"
            else:
                sub_string = (
                    f"{sub_string}{'    ' * any_depth}{key}: {str(value[key])}\n"
                )
        return sub_string
