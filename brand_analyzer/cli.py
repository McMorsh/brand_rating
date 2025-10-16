# Command Line Interface

import argparse
import sys
from pathlib import Path

from brand_analyzer import REPORTS
from brand_analyzer import read_csv


def parse_arguments():
    parser = argparse.ArgumentParser(description='Brand analyzer')
    parser.add_argument("--files", "-f", nargs='+', required=True, help="input files")
    parser.add_argument("--report", "-r", required=True, help="report files")

    return parser


def main():
    args = parse_arguments().parse_args()

    arr_path = [Path(path) for path in args.files]

    try:
        items = read_csv(arr_path)
    except FileNotFoundError as e:
        print(f"ERROR: File not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unable to read: {e}")
        sys.exit(2)

    if not items:
        print("ERROR: File empty.")
        sys.exit(3)

    name = args.report
    cls = REPORTS[name]
    if cls is None:
        raise Exception(f"No report file named {name}")

    rows = cls.generate(items)
    cls.display(rows)


if __name__ == "__main__":
    main()
