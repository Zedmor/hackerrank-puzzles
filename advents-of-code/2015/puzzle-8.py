def convert_line(line: str) -> str:
    """
    >>> convert_line('"\\\\x27"')
    """
    print(line)
    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    line = '"' + line + '"'
    print(len(line))
    return line


def main():
    """
    >>> main()
    """
    with open('input-8.txt') as file:
        all_chars = 0
        counter = 0
        for line in file.readlines():
            line = line[:-1]
            print(line)
            print(len(line))
            all_chars += len(line)
            line = convert_line(line)
            counter += len(line)
            print(line)

    print(all_chars - counter)


if __name__ == "__main__":
    main()
