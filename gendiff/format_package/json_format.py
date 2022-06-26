def json_format(diff_dict):
    def make_sub_string(sub_dict, sub_string, depth):
        sorted_tuple = sorted(sub_dict.items(), key=lambda x: x[0])
        sub_dict = dict(sorted_tuple)
        for index, key in enumerate(sub_dict):
            if isinstance(sub_dict[key], dict):
                sub_string += "  " * depth + '"' + key + '": {\n'
                sub_string = (
                    make_sub_string(sub_dict[key], sub_string, depth + 1)
                    + "  " * depth
                    + "}"
                )
            elif isinstance(sub_dict[key], tuple):
                sub_string += (
                    "  " * depth + '"' + key + '": "' + str(sub_dict[key]) + '"'
                )
            if index < len(sub_dict) - 1:
                sub_string += ","
            sub_string += "\n"
        return sub_string

    result = make_sub_string(diff_dict, "{\n", 1) + "}"
    return result
