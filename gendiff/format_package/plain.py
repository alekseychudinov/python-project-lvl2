def plain(diff_dict):

    def make_sub_string(sub_dict, sub_string, path_name):
        sorted_tuple = sorted(sub_dict.items(), key=lambda x: x[0])
        sub_dict = dict(sorted_tuple)
        for key in sub_dict:
            if isinstance(sub_dict[key], tuple):
                if len(sub_dict[key][0]) == 0:
                    sub_string += "Property '" + path_name + str(key) + "' was added with value: " + map_value(sub_dict[key][1]['value']) + "\n"
                elif len(sub_dict[key][1]) == 0:
                    sub_string += "Property '" + path_name + key + "' was removed\n"
                elif sub_dict[key][0] != sub_dict[key][1]:
                    sub_string += "Property '" + path_name + key + "' was updated. From " + map_value(sub_dict[key][0]['value']) + " to " + map_value(sub_dict[key][1]['value']) + "\n"
            elif isinstance(sub_dict[key], dict):
                sub_string = make_sub_string(sub_dict[key], sub_string, path_name + key + ".")
        return sub_string

    result = make_sub_string(diff_dict, "", "")
    return result


def map_value(key_value):
    if isinstance(key_value, dict):
        return "[complex value]"
    elif str(key_value) == 'True':
        return "true"
    elif str(key_value) == 'False':
        return "false"
    elif str(key_value) == 'None':
        return "null"
    else:
        return "'" + str(key_value) + "'"
