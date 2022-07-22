def plain(diff_dict):
    result = make_sub_string(diff_dict["children"], "", "")
    return result.rstrip(result[-1])


def make_sub_string(sub_list, sub_string, path_name):
    for item_dict in sub_list:
        name_of_property = item_dict["key"]
        type_of_property = item_dict["type"]
        prefix = f"Property '{path_name}{name_of_property}'"
        if type_of_property == "added":
            value_of_property = item_dict["value"]
            sub_string = f"{sub_string}{prefix} was added with value: {map_value(value_of_property)}\n" # noqa
        elif type_of_property == "deleted":
            sub_string = f"{sub_string}{prefix} was removed\n"
        elif type_of_property == "updated":
            value_of_property1 = item_dict["value1"]
            value_of_property2 = item_dict["value2"]
            sub_string = (
                f"{sub_string}{prefix} was updated. From "
                f"{map_value(value_of_property1)} to {map_value(value_of_property2)}\n" # noqa
            )
        elif type_of_property == "parent":
            list_of_children = item_dict["children"]
            sub_string = make_sub_string(
                list_of_children, sub_string, path_name + name_of_property + "."
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
