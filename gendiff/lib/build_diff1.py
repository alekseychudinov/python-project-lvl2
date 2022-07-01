def build_diff(dict1, dict2):
    for key in dict2:
        if (
            key in dict1
            and isinstance(dict1[key], dict)
            and isinstance(dict2[key], dict)
        ):
            build_diff(dict1[key], dict2[key])
        elif key in dict1:
            dict1[key] = ({"value": dict1[key]}, {"value": dict2[key]})
        else:
            dict1[key] = ({}, {"value": dict2[key]})
    for key in dict1:
        if key not in dict2:
            dict1[key] = ({"value": dict1[key]}, {})
    return dict1
