import argparse
from gendiff import generate_diff


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

    # print(f"Loaded data keys: {list(data1.items())} and {list(data2.items())}")
    # print(f"Comparing {file1_path} and {file2_path} with format {args.format}")

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == '__main__':
    main()