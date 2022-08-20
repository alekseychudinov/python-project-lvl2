def stylish(diff_dict):
    return build_diff(diff_dict, 1)


def build_diff(tree, depth):  # noqa: C901
    children = tree.get('children')
    key = tree.get('key')
    value = value_to_str(tree.get('value'), depth)
    value1 = value_to_str(tree.get('value1'), depth)
    value2 = value_to_str(tree.get('value2'), depth)
    indent = build_indent(depth - 1)
    if tree["type"] == "root":
        result = "{\n"
        for item_list in children:
            result = f"{result}{build_diff(item_list, depth)}"
        return f"{result}}}"
    else:
        type_of_property = tree["type"]
        if type_of_property == "parent":
            result = f"{build_indent(depth)}{key}: {{\n"
            for item_list in tree["children"]:
                result = f"{result}{build_diff(item_list, depth + 1)}"
            return f"{result}{build_indent(depth)}}}\n"
        elif type_of_property == "added":
            return f"{indent}  + {key}: {value}\n"
        elif type_of_property == "deleted":
            return f"{indent}  - {key}: {value}\n"
        elif type_of_property == "unchanged":
            return f"{indent}    {key}: {value}\n"
        elif type_of_property == "updated":
            return f"{indent}  - {key}: {value1}\n{indent}  + {key}: {value2}\n"
        else:
            return 'Неизвестный тип свойства'


def value_to_str(key_value, depth):
    if isinstance(key_value, dict):
        return map_dict_value(key_value, "{\n", depth + 1) + build_indent(depth) + "}" # noqa
    elif isinstance(key_value, bool):
        return 'true' if key_value else 'false'
    elif key_value is None:
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


def build_indent(indent):
    return " " * 4 * indent
