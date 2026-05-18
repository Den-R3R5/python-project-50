import argparse


def arg_parse():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")  # positional argument
    parser.add_argument("second_file")
    return parser.parse_args()
