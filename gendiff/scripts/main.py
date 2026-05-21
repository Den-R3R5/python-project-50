from gendiff import arg_parse, generate_diff, parse


def main():
    args = arg_parse()
    first_file, second_file = parse(args.first_file, args.second_file)
    diff = generate_diff(first_file, second_file, args.format)
    print(args.format)
    print(diff)


if __name__ == "__main__":
    main()
