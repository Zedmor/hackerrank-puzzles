import re
from enum import Enum

import numpy as np

matrix = np.zeros((1000, 1000))


class Commands(Enum):
    TURN_ON = 1
    TURN_OFF = 2
    TOGGLE = 3


def parse_command(command):
    """
    >>> parse_command('turn on 887,9 through 959,629')
    [<Commands.TURN_ON: 1>, (887, 9), (959, 629)]
    >>> parse_command('toggle 944,498 through 995,928')
    [<Commands.TOGGLE: 3>, (944, 498), (995, 928)]


    """
    lookup = {'turn on': Commands.TURN_ON, 'turn off': Commands.TURN_OFF, 'toggle': Commands.TOGGLE}
    parsed = re.findall('(turn off|turn on|toggle)\s+(\d+),(\d+) through (\d+),(\d+)', command)[0]
    return [lookup[parsed[0]], (int(parsed[1]), int(parsed[2])), (int(parsed[3]) + 1, int(parsed[4]) + 1)]


def execute_command(command):
    for i in range(command[1][0], command[2][0]):
        for j in range(command[1][1], command[2][1]):
            if command[0] == Commands.TURN_ON:
                matrix[i, j] = matrix[i, j] + 1
            elif command[0] == Commands.TURN_OFF:
                matrix[i, j] = max(matrix[i, j] - 1, 0)
            elif command[0] == Commands.TOGGLE:
                matrix[i, j] = matrix[i, j] + 2

# execute_command(parse_command('toggle 0,0 through 999,0'))
# print(matrix)

def calculate_lights():
    all_lights = 0
    for i in range(1000):
        for j in range(1000):
            all_lights += matrix[i, j]
    return all_lights



def main():
    """
    >>> main()
    """
    with open('input-6.txt') as file:
        for line in file.readlines():
            execute_command(parse_command(line))
        print(calculate_lights())


