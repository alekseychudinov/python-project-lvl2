def stylish(diff_dict):
    def make_sub_string(sub_dict, sub_string, depth):
        sorted_tuple = sorted(sub_dict.items(), key=lambda x: x[0])
        sub_dict = dict(sorted_tuple)
        for key in sub_dict:
            if isinstance(sub_dict[key], dict):
                sub_string += "    " * depth + key + ": {\n"
                sub_string = (
                    make_sub_string(sub_dict[key], sub_string, depth + 1)
                    + "    " * depth
                    + "}\n"
                )
            elif isinstance(sub_dict[key], tuple):
                if len(sub_dict[key][0]) == 0:
                    sub_string += (
                        "    " * (depth - 1)
                        + "  + "
                        + key
                        + ": "
                        + map_value(sub_dict[key][1]["value"], depth)
                        + "\n"
                    )
                elif len(sub_dict[key][1]) == 0:
                    sub_string += (
                        "    " * (depth - 1)
                        + "  - "
                        + key
                        + ": "
                        + map_value(sub_dict[key][0]["value"], depth)
                        + "\n"
                    )
                elif sub_dict[key][0]["value"] == sub_dict[key][1]["value"]:
                    sub_string += (
                        "    " * (depth - 1)
                        + "    "
                        + key
                        + ": "
                        + map_value(sub_dict[key][0]["value"], depth)
                        + "\n"
                    )
                else:
                    sub_string += (
                        "    " * (depth - 1)
                        + "  - "
                        + key
                        + ": "
                        + map_value(sub_dict[key][0]["value"], depth)
                        + "\n"
                    )
                    sub_string += (
                        "    " * (depth - 1)
                        + "  + "
                        + key
                        + ": "
                        + map_value(sub_dict[key][1]["value"], depth)
                        + "\n"
                    )
        return sub_string

    result = make_sub_string(diff_dict, "{\n", 1) + "}"
    return result


def map_value(key_value, depth):
    def map_dict_value(value, sub_string, any_depth):
        if isinstance(value, dict):
            for key in value:
                if isinstance(value[key], dict):
                    sub_string += "    " * any_depth + key + ": {\n"
                    sub_string = (
                        map_dict_value(value[key], sub_string, any_depth + 1)
                        + "    " * any_depth
                        + "}\n"
                    )
                else:
                    sub_string += (
                        "    " * any_depth + key + ": " + str(value[key]) + "\n"
                    )
            return sub_string

    if isinstance(key_value, dict):
        return map_dict_value(key_value, "{\n", depth + 1) + "    " * depth + "}"
    elif str(key_value) == "True":
        return "true"
    elif str(key_value) == "False":
        return "false"
    elif str(key_value) == "None":
        return "null"
    else:
        return str(key_value)
