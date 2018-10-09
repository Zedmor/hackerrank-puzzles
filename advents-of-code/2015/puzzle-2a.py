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

from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def calculate_visited(commands):
    """
    >>> calculate_visited('^v')
    3
    >>> calculate_visited('^>v<')
    3
    >>> calculate_visited('^v^v^v^v^v')
    11
    """
    command_sequence = map(process_char, commands)

    visited = {(0, 0)}

    # print(list(command_sequence))
    x1 = y1 = x2 = y2 = 0
    for command1, command2 in grouper(command_sequence, 2):
        x1, y1 = update_coord(x1, y1, command1)
        visited.add((x1, y1))
        x2, y2 = update_coord(x2, y2, command2)
        visited.add((x2, y2))
    return len(visited)



def main():
    with open('input-3.txt') as file:
        commands = file.readline()
        print(calculate_visited(commands))

if __name__ == "__main__":
    main()
