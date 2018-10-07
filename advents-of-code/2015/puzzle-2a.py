def process_char(char):
    if char == '^':
        return 0, -1
    elif char == 'v':
        return 0, 1
    elif char == '>':
        return 1, 0
    elif char == '<':
        return -1, 0
    else:
        raise ValueError


def update_coord(x, y, command):
    return x + command[0], y + command[1]


def main():
    with open('input-3.txt') as file:
        commands = file.readline()
        command_sequence = map(process_char, commands)

        visited = set((0, 0))

        # print(list(command_sequence))
        x = y = 0
        for command in command_sequence:
            x, y = update_coord(x, y, command)
            visited.add((x, y))
    print(len(visited))

if __name__ == "__main__":
    main()
