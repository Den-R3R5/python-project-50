from gendiff import (
    arg_parse,
    gendiff,
)


def main():
    parse = arg_parse()
    gendiff(parse.first_file, parse.second_file)


if __name__ == "__main__":
    main()
