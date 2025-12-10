import argparse
import json

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
        help='set format of output'
    )

    args = parser.parse_args()

    file1_path = args.first_file
    file2_path = args.second_file

    with open(file1_path) as f1, open(file2_path) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    print(f"Loaded data keys: {list(data1.keys())} and {list(data2.keys())}")
    print(f"Comparing {file1_path} and {file2_path} with format {args.format}")

if __name__ == '__main__':
    main()