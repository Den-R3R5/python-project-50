from gendiff import arg_parse, generate_diff


def main():
    args = arg_parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(args.format)
    print(diff)


if __name__ == "__main__":
    main()
