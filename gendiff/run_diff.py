from gendiff import generate_diff
from gendiff.file_parser import file_parser
from gendiff.formatters import DEFAULT_FORMAT, get_formatter


def run_diff(file_path1, file_path2, format_name=DEFAULT_FORMAT):
    data1 = file_parser(file_path1)
    data2 = file_parser(file_path2)
    formatter = get_formatter(format_name)
    diff_tree = generate_diff(data1, data2)
    return formatter(diff_tree)

# print(run_diff(
#     "../tests/test_data_json/4.0.json", "../tests/test_data_json/4.1.json" ))