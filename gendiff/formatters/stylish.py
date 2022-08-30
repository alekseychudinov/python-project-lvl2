def render_stylish(diff):
    return tree_to_stylish(diff, 1)


def tree_to_stylish(tree, depth):  # noqa: C901
    children = tree.get("children")
    key = tree.get("key")
    value = value_to_str(tree.get("value"), depth)
    value1 = value_to_str(tree.get("value1"), depth)
    value2 = value_to_str(tree.get("value2"), depth)
    indent = build_indent(depth - 1)
    indent_big = build_indent(depth)
    type_of_property = tree["type"]
    if type_of_property == "root":
        lines = map(lambda child: tree_to_stylish(child, depth), children)
        result = "".join(lines)
        return f"{{\n{result}}}"
    elif type_of_property == "parent":
        lines = map(lambda child: tree_to_stylish(child, depth + 1), children)
        result = "".join(lines)
        return f"{indent_big}{key}: {{\n{result}{indent_big}}}\n"
    elif type_of_property == "added":
        return f"{indent}  + {key}: {value}\n"
    elif type_of_property == "deleted":
        return f"{indent}  - {key}: {value}\n"
    elif type_of_property == "unchanged":
        return f"{indent}    {key}: {value}\n"
    elif type_of_property == "updated":
        return f"{indent}  - {key}: {value1}\n{indent}  + {key}: {value2}\n"
    else:
        return "Неизвестный тип свойства"


def value_to_str(value, depth):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, dict):
        indent = build_indent(depth)
        indent_big = build_indent(depth + 1)
        for key in value:
            print('value=', value)
            print('key=', key)
            print('value[key]=', value[key])
            return f"{{\n{indent_big}{key}: {value_to_str(value[key], depth + 1)}\n{indent}}}" # noqa
    else:
        return str(value)


def build_indent(indent):
    return " " * 4 * indent
