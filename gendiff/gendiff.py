from gendiff.lib.formatter import formatting
from gendiff.lib.parser import parse
from gendiff.lib.tree import make_tree


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    return formatting(make_tree(file1, file2), format_name)
