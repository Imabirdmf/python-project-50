from gendiff import generate_diff
from gendiff.file_parser import file_parser


def run_diff(file_path1, file_path2):
    data1 = file_parser(file_path1)
    data2 = file_parser(file_path2)
    return generate_diff(data1, data2)
