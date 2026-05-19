from gendiff import (
    arg_parse,
    generate_diff,
)


def main():
    parse = arg_parse()
    diff = generate_diff(parse.first_file, parse.second_file)
    print(diff)


if __name__ == "__main__":
    main()
