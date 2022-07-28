from gendiff.formatters.stylish import build_indent, get_value


def json_format(diff_dict):
    string = f"{{\n    \"type\": \"{diff_dict['type']}\",\n    \"children\": [\n" # noqa
    string = make_sub_string(diff_dict["children"], string, 2) + "]"
    return f"{string}\n}}"


def make_sub_string(sub_list, sub_string, depth):
    for index, item_dict in enumerate(sub_list):
        name_of_property = item_dict["key"]
        type_of_property = item_dict["type"]
        sub_string = (
            f"{sub_string}{build_indent(depth - 1)}{{\n"
            f'{build_indent(depth)}"key": "{name_of_property}",\n'
            f'{build_indent(depth)}"type": "{type_of_property}",\n'
        )
        if type_of_property == "parent":
            list_of_children = item_dict["children"]
            sub_string = f'{sub_string}{build_indent(depth)}"children": [\n'
            sub_string = (
                make_sub_string(list_of_children, sub_string, depth + 1) + "]\n"
            )
        elif type_of_property in ("deleted", "added", "unchanged"):
            sub_string = f'{sub_string}{build_indent(depth)}"value":{map_value(get_value(item_dict), depth)}\n' # noqa
        elif type_of_property == "updated":
            sub_string = (
                f'{sub_string}{build_indent(depth)}"value1":{map_value(get_value(item_dict)[0], depth)},\n' # noqa
                f'{build_indent(depth)}"value2":{map_value(get_value(item_dict)[1], depth)}\n' # noqa
            )
        sub_string = f"{sub_string}{build_indent(depth - 1)}}}"
        if index < len(sub_list) - 1:
            sub_string += ",\n"
    return sub_string


def map_value(key_value, depth):
    if isinstance(key_value, dict):
        indent = f"\n{build_indent(depth)}{{\n"
        return f'{map_dict_value(key_value, indent, depth + 1)}{"    " * depth}}}' # noqa
    elif str(key_value) == "True":
        return " true"
    elif str(key_value) == "False":
        return " false"
    elif str(key_value) == "None":
        return " null"
    elif isinstance(key_value, int):
        return f' {str(key_value)}'
    else:
        return f' "{str(key_value)}"'


def map_dict_value(value_dict, sub_string, any_depth):
    for i, key in enumerate(value_dict):
        sub_string = f'{sub_string}{build_indent(any_depth)}"{key}":'
        if isinstance(value_dict[key], dict):
            sub_string = f"{sub_string}\n" f"{build_indent(any_depth)}{{\n"
            sub_string = f"{map_dict_value(value_dict[key], sub_string, any_depth + 1)}{build_indent(any_depth)}}}" # noqa
        else:
            sub_string = f"{sub_string}{map_value(value_dict[key], any_depth)}"
        if i < len(value_dict) - 1:
            sub_string += ","
        sub_string += "\n"
    return sub_string
