import re

import numpy as np


def rect(a, b, screen):
    print(f"Creating rectangle {a} by {b}")
    screen[:b, :a] = 1


def rotate(obj, n, by, screen):
    print(f"Rotating {obj} {n} by {by}")
    if obj == "row":
        screen[n] = np.roll(screen[n], by)
    else:
        screen[:, n] = np.roll(screen[:, n], by)

    print(screen)


def run(commands, screen):
    for command in commands:
        if "rect" in command:
            a, b = re.findall(r"(\d+)x(\d+)", command)[0]
            rect(int(a), int(b), screen)
        elif "column" in command:
            col, by = re.findall(r"(\d+)\sby\s(\d+)", command)[0]
            rotate("column", int(col), int(by), screen)
        elif "row" in command:
            row, by = re.findall(r"(\d+)\sby\s(\d+)", command)[0]
            rotate("row", int(row), int(by), screen)


def test_run():
    commands = ["rect 3x2",
                "rotate column x=1 by 1",
                "rotate row y=0 by 4",
                "rotate column x=1 by 1"]

    screen = np.zeros((3, 7))
    print()
    print(screen)

    run(commands, screen)

def test_real_run():
    with open("day_8.txt") as inp_file:
        commands = inp_file.readlines()

    screen = np.zeros((6, 50))
    run(commands, screen)

    print(screen.sum())
    print('\n'.join('\t'.join('#' if x else ' ' for x in y) for y in screen))