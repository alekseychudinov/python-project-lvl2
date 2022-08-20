from gendiff.formatters.stylish import build_indent


def json_format(diff_dict):
    string = f"{{\n    \"type\": \"{diff_dict['type']}\",\n    \"children\": [\n" # noqa
    string = make_sub_string(diff_dict["children"], string, 2) + "]"
    return f"{string}\n}}"


def make_sub_string(sub_list, sub_string, depth):
    for index, item_dict in enumerate(sub_list):
        indent = build_indent(depth)
        value = value_to_str(item_dict.get('value'), depth)
        value1 = value_to_str(item_dict.get('value1'), depth)
        value2 = value_to_str(item_dict.get('value2'), depth)
        key = item_dict.get('key')
        type = item_dict.get('type')
        sub_string = (
            f"{sub_string}{build_indent(depth - 1)}{{\n"
            f'{indent}"key": "{key}",\n'
            f'{indent}"type": "{type}",\n'
        )
        if type == "parent":
            list_of_children = item_dict["children"]
            sub_string = f'{sub_string}{indent}"children": [\n'
            sub_string = (
                make_sub_string(list_of_children, sub_string, depth + 1) + "]\n"
            )
        elif type in ("deleted", "added", "unchanged"):
            sub_string = f'{sub_string}{indent}"value":{value}\n'
        elif type == "updated":
            sub_string = (
                f'{sub_string}{indent}"value1":{value1},\n'
                f'{indent}"value2":{value2}\n'
            )
        else:
            return 'Неизвестный тип свойства'
        sub_string = f"{sub_string}{build_indent(depth - 1)}}}"
        if index < len(sub_list) - 1:
            sub_string += ",\n"
    return sub_string


def value_to_str(key_value, depth):
    if isinstance(key_value, dict):
        indent = f"\n{build_indent(depth)}{{\n"
        return f'{map_dict_value(key_value, indent, depth + 1)}{"    " * depth}}}' # noqa
    elif isinstance(key_value, bool):
        return ' true' if key_value else ' false'
    elif key_value is None:
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
            sub_string = f"{sub_string}{value_to_str(value_dict[key], any_depth)}"
        if i < len(value_dict) - 1:
            sub_string += ","
        sub_string += "\n"
    return sub_string
