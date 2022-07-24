def stylish(diff_dict):
    return build_diff(diff_dict, 1)


def build_diff(tree, depth):  # noqa: C901
    if tree["type"] == "root":
        result = "{\n"
        for item_list in tree["children"]:
            result = f"{result}{build_diff(item_list, depth)}"
        return f"{result}}}"
    else:
        name_of_property = tree["key"]
        type_of_property = tree["type"]
        if type_of_property == "parent":
            result = f"{build_indent(depth)}{name_of_property}: {{\n"
            for item_list in tree["children"]:
                result = f"{result}{build_diff(item_list, depth + 1)}"
            return f"{result}{build_indent(depth)}}}\n"
        elif type_of_property == "added":
            return f"{build_indent(depth - 1)}  + {name_of_property}: {map_value(get_value(tree), depth)}\n" # noqa
        elif type_of_property == "deleted":
            return f"{build_indent(depth - 1)}  - {name_of_property}: {map_value(get_value(tree), depth)}\n" # noqa
        elif type_of_property == "unchanged":
            return f"{build_indent(depth - 1)}    {name_of_property}: {map_value(get_value(tree), depth)}\n" # noqa
        elif type_of_property == "updated":
            return f"{build_indent(depth - 1)}  - {name_of_property}: {map_value(get_value(tree)[0], depth)}\n{build_indent(depth - 1)}  + {name_of_property}: {map_value(get_value(tree)[1], depth)}\n" # noqa


def map_value(key_value, depth):
    if isinstance(key_value, dict):
        return map_dict_value(key_value, "{\n", depth + 1) + build_indent(depth) + "}" # noqa
    elif str(key_value) == "True":
        return "true"
    elif str(key_value) == "False":
        return "false"
    elif str(key_value) == "None":
        return "null"
    else:
        return str(key_value)


def map_dict_value(value, sub_string, any_depth):
    for key in value:
        if isinstance(value[key], dict):
            sub_string = f"{sub_string}{build_indent(any_depth)}{key}: {{\n"
            sub_string = f"{map_dict_value(value[key], sub_string, any_depth + 1)}{build_indent(any_depth)}}}\n" # noqa
        else:
            sub_string = (
                f"{sub_string}{build_indent(any_depth)}{key}: {str(value[key])}\n" # noqa
            )
    return sub_string


def build_indent(x):
    return "	" * x


def get_value(my_dict):
    if my_dict["type"] in ("deleted", "added", "unchanged"):
        return my_dict["value"]
    elif my_dict["type"] == "updated":
        return my_dict["value1"], my_dict["value2"]
