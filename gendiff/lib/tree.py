def make_tree(data1, data2):
    return {"type": "root", "children": make_children(data1, data2)}


def make_children(data1, data2):
    result = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data2:
            result.append({"key": key, "type": "deleted", "value": data1[key]})
        elif key not in data1:
            result.append({"key": key, "type": "added", "value": data2[key]})
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append(
                    {
                        "key": key,
                        "type": "parent",
                        "children": make_children(data1[key], data2[key]),
                    }
                )
            elif data1[key] == data2[key]:
                result.append({"key": key, "type": "unchanged", "value": data1[key]}) # noqa
            else:
                result.append(
                    {
                        "key": key,
                        "type": "updated",
                        "value1": data1[key],
                        "value2": data2[key],
                    }
                )
    return result
