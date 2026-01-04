import argparse

from gendiff.formatters import DEFAULT_FORMAT
from gendiff.run_diff import run_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        prog="gendiff",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default=DEFAULT_FORMAT, help="set format of output"
    )

    args = parser.parse_args()

    print(run_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
