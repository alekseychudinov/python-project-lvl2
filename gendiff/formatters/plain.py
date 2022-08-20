def plain(diff_dict):
    result = make_sub_string(diff_dict["children"], "", "")
    return result.rstrip(result[-1])


def make_sub_string(sub_list, sub_string, path_name):  # noqa: C901
    for item_dict in sub_list:
        key = item_dict.get('key')
        type = item_dict.get('type')
        prefix = f"Property '{path_name}{key}'"
        if type == "added":
            value = value_to_str(item_dict.get('value'))
            sub_string = f"{sub_string}{prefix} was added with value: {value}\n"
        elif type == "deleted":
            sub_string = f"{sub_string}{prefix} was removed\n"
        elif type == "updated":
            value1 = value_to_str(item_dict.get('value1'))
            value2 = value_to_str(item_dict.get('value2'))
            sub_string = (
                f"{sub_string}{prefix} was updated. From "
                f"{value1} to {value2}\n" # noqa
            )
        elif type == "parent":
            list_of_children = item_dict["children"]
            sub_string = make_sub_string(
                list_of_children, sub_string, path_name + key + "."
            )
        elif type != "unchanged":
            print(type, '\n')
            return 'Неизвестный тип свойства'
    return sub_string


def value_to_str(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif isinstance(key_value, bool):
        return 'true' if key_value else 'false'
    elif key_value is None:
        return "null"
    elif isinstance(key_value, int):
        return str(key_value)
    else:
        return f"'{str(key_value)}'"
