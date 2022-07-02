from gendiff.lib.build_diff import build
from gendiff.lib.cli import parse_args
from gendiff.lib.formatter import formatting
from gendiff.lib.parser import parse


def generate_diff():
    file1, file2, format_name = parse(parse_args())
    result_dict = build(file1, file2)
    return formatting(format_name, result_dict)
