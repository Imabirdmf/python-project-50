import argparse
import json
from itertools import zip_longest


# first_file = 'files/file1.json'
# second_file = 'files/file2.json'

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        prog='gendiff'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='json',
        help='set format of output'
    )

    args = parser.parse_args()

    file1_path = args.first_file
    file2_path = args.second_file

    generate_diff(file1_path, file2_path)
    # print(f"Loaded data keys: {list(data1.items())} and {list(data2.items())}")
    # print(f"Comparing {file1_path} and {file2_path} with format {args.format}")

def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)


        result = '{\n'
        for k in sorted(max(data1, data2, key=len)):
            if data1.get(k) is None:
                result += f'+ {k}: {data2[k]}\n'
            elif data2.get(k) is None:
                result += f'- {k}: {data1[k]}\n'
            elif data1.get(k) == data2.get(k):
                result += f'  {k}: {data1[k]}\n'
            elif data1.get(k) != data2.get(k):
                result += f'- {k}: {data1[k]}\n'\
                      f'+ {k}: {data2[k]}\n'
        result += '}'
        print(result)


if __name__ == '__main__':
    main()