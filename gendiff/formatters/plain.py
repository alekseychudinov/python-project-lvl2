def render_plain(diff):
    result = node_processing(diff)
    return result.rstrip(result[-1])


def node_processing(node, parent_path = ''):
    children = node.get('children')
    property_path = f"{parent_path}{node.get('key')}"
    for child in children:
        type = child.get("type")
        prefix = f"Property '{property_path}'"
        if type == "added":
            value = value_to_str(child.get("value"))
            return f"{prefix} was added with value: {value}\n"
        elif type == "deleted":
            return f"{prefix} was removed\n"
        elif type == "updated":
            value1 = value_to_str(child.get("value1"))
            value2 = value_to_str(child.get("value2"))
            return (
                f"{prefix} was updated. From "
                f"{value1} to {value2}\n"
            )
        elif type == "parent":
            lines = map(lambda child2: node_processing(child2, f"{property_path}."), children)
            return '\n'.join(filter(bool, lines))
        elif type != "unchanged":
            return "Неизвестный тип свойства"


def value_to_str(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif isinstance(key_value, bool):
        return "true" if key_value else "false"
    elif key_value is None:
        return "null"
    elif isinstance(key_value, int):
        return str(key_value)
    else:
        return f"'{str(key_value)}'"
