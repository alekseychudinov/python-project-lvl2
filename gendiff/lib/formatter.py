from gendiff.formatters.json_format import render_json_format
from gendiff.formatters.plain import render_plain
from gendiff.formatters.stylish import render_stylish


def formatting(result_dict, format_name):
    if format_name == "stylish":
        return render_stylish(result_dict)
    elif format_name == "plain":
        return render_plain(result_dict)
    elif format_name == "json":
        return render_json_format(result_dict)
    else:
        return "Неизвестный формат для вывода результата сравнения"
