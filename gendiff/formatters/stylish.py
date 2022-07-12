def stylish(diff_dict):
    return make_sub_string(diff_dict["children"], "{\n", 1) + "}"


def make_sub_string(sub_list, sub_string, depth):
    for item_dict in sub_list:
        name_of_property = item_dict["key"]
        type_of_property = item_dict["type"]
        if type_of_property == "parent":
            list_of_children = item_dict["children"]
            sub_string += build_indent(depth) + name_of_property + ": {\n"
            sub_string = (
                make_sub_string(list_of_children, sub_string, depth + 1)
                + build_indent(depth)
                + "}\n"
            )
        elif type_of_property == "added":
            sub_string = (
                f"{sub_string}{build_indent(depth - 1)}  + {name_of_property}: "
                f"{map_value(get_value(item_dict), depth)}\n"
            )
        elif type_of_property == "deleted":
            sub_string = (
                f"{sub_string}{build_indent(depth - 1)}  - {name_of_property}: "
                f"{map_value(get_value(item_dict), depth)}\n"
            )
        elif type_of_property == "unchanged":
            sub_string = (
                f"{sub_string}{build_indent(depth - 1)}    {name_of_property}: "
                f"{map_value(get_value(item_dict), depth)}\n"
            )
        elif type_of_property == "updated":
            sub_string = (
                f"{sub_string}{build_indent(depth - 1)}  - {name_of_property}: "
                f"{map_value(get_value(item_dict)[0], depth)}\n"
            )
            sub_string = (
                f"{sub_string}{build_indent(depth - 1)}  + {name_of_property}: "
                f"{map_value(get_value(item_dict)[1], depth)}\n"
            )
    return sub_string


def map_value(key_value, depth):
    if isinstance(key_value, dict):
        return map_dict_value(key_value, "{\n", depth + 1) + build_indent(depth) + "}"
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
                sub_string = f"{sub_string}{build_indent(any_depth)}{key}: {{\n"
                sub_string = f"{map_dict_value(value[key], sub_string, any_depth + 1)}{build_indent(any_depth)}}}\n"
            else:
                sub_string = (
                    f"{sub_string}{build_indent(any_depth)}{key}: {str(value[key])}\n"
                )
        return sub_string


def build_indent(x):
    return "    " * x


def get_value(my_dict):
    if my_dict["type"] in ("deleted", "added", "unchanged"):
        return my_dict["value"]
    elif my_dict["type"] == "updated":
        return my_dict["value1"], my_dict["value2"]
