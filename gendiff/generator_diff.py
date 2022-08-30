from gendiff.lib.formatter import formatting
from gendiff.lib.parser import get_data
from gendiff.lib.tree import make_tree


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file1 = get_data(file_path1)
    file2 = get_data(file_path2)
    return formatting(make_tree(file1, file2), format_name)
    #result = make_tree(file1, file2)
    #print(result, '\n')
    #return formatting(result, format_name)