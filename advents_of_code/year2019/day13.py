import os
from itertools import zip_longest
from time import sleep

from advents_of_code.common import Computer

clear = lambda: os.system('clear') #on Linux System
clear()

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

FILE_PATH = '/home/zedmor/Development/hackerrank-puzzles/advents_of_code/2019/day13.txt'



class Game:
    tiles = {0: ' ',
             1: 'X',
             2: '#',
             3: '_',
             4: 'o'}

    def __init__(self):
        self.score = 0

        self.field = [[' '] * 42 for i in range(24)]

        with open(FILE_PATH) as data:
            program = list(map(int, data.read().split(',')))

        self.c = Computer(program, wait_for_input=True)

        self.paddle = 0
        self.ball = 0

        self.c.program[0] = 2

    def display_field(self, field, result):
        for x, y, t in grouper(3, result):
            if x == -1 and y == 0:
                self.score = t
            else:
                field[y][x] = self.tiles[t]
                if t == 3:
                    self.paddle = x
                if t == 4:
                    self.ball = x

        print('SCORE: {}'.format(self.score))
        for line in field:
            print(''.join(line))

    def run(self):
        while True:
            try:
                self.c.run_software()
            except ValueError:
                clear()
                result = self.c.outputs
                self.c.outputs = []
                self.display_field(self.field, result)
                self.c.inputs.append(self.move_paddle())
            if self.c.terminated:
                clear()
                result = self.c.outputs
                self.c.outputs = []
                self.display_field(self.field, result)
                self.c.inputs.append(self.move_paddle())
                break

    def move_paddle(self):
        if self.paddle > self.ball:
            return -1
        elif self.paddle < self.ball:
            return 1
        return 0


if __name__ == '__main__':
    game = Game()
    game.run()
    print(game.score)

