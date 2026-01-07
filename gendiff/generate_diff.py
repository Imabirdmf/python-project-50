from gendiff.diff_logic import dict_diff
from gendiff.file_parser import file_parser
from gendiff.formatters import DEFAULT_FORMAT, get_formatter


def generate_diff(file_path1, file_path2, format_name=DEFAULT_FORMAT):
    data1 = file_parser(file_path1)
    data2 = file_parser(file_path2)
    formatter = get_formatter(format_name)
    diff_tree = dict_diff(data1, data2)
    # print(diff_tree)
    return formatter(diff_tree)


# print(generate_diff(
#     "../tests/test_data_yaml/1.0.yaml", "../tests/test_data_yaml/1.0.yml" ))
