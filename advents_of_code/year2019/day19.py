from advents_of_code.year2019.day18.intcode import IntCode, OutputInterrupt
import sys,tty,termios

program = """109,424,203,1,21102,11,1,0,1105,1,282,21101,18,0,0,1106,0,259,1202,1,1,221,203,1,21101,0,31,0,1106,0,282,21102,38,1,0,1105,1,259,20101,0,23,2,22102,1,1,3,21102,1,1,1,21102,57,1,0,1105,1,303,2101,0,1,222,21002,221,1,3,20101,0,221,2,21102,1,259,1,21101,0,80,0,1105,1,225,21102,40,1,2,21101,0,91,0,1105,1,303,1201,1,0,223,20101,0,222,4,21101,0,259,3,21101,0,225,2,21101,0,225,1,21102,118,1,0,1105,1,225,21001,222,0,3,21102,1,144,2,21101,0,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1105,1,259,1202,1,1,223,20101,0,221,4,21001,222,0,3,21102,1,14,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,106,0,109,20207,1,223,2,20101,0,23,1,21101,0,-1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22101,0,-3,1,21201,-2,0,2,22101,0,-1,3,21101,0,250,0,1105,1,225,21202,1,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21102,384,1,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2106,0,0"""

x = 1321
y = 669


def get_wall(x, y):
    comp = IntCode(program=program)
    comp.input_queue.append(y)
    comp.input_queue.append(x)

    while not comp.done:
        try:
            comp.run()
        except OutputInterrupt:
            pass
            # print("Sensor BOOST code: ", comp.output_queue[-1])

    if comp.output_queue[-1]:
        return '#'
    else:
        return '.'

from random import randint, choice
import subprocess
import platform
import time


class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = set()
        self.explored = set()
        self.goal = (width - 1, height - 1)
        self.player = (0, 0)
        self.screens_right = 0
        self.screens_down = 0

    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = (x, y)

        if d[0] == 'r':
            pos = (x + 1, y)
            if pos[0] % self.width == 0:
                self.screens_right += 1
        if d[0] == 'l' and x > 0:
            if x % self.width == 0 and self.screens_right > 0:
                self.screens_right -= 1
            if x > 0:
                pos = (x - 1, y)
        if d[0] == 'u':
            if y % self.height == 0 and self.screens_down > 0:
                self.screens_down -= 1
            elif y > 0:
                pos = (x, y - 1)
        if d[0] == 'd':
            pos = (x, y + 1)
            if pos[1] % self.height == 0:
                self.screens_down += 1

        if pos not in self.explored:
            item = get_wall(*pos)
            if item == '#':
                self.walls.add(pos)
            self.explored.add(pos)

        # if pos not in self.walls:
        self.player = pos

        if pos == self.goal:
            print("You made it to the end!")


def draw_grid(g, width=2):
    for y in range(g.height):
        for x in range(g.width):
            new_x = x + 50 * g.screens_right
            new_y = y + 50 * g.screens_down
            if (new_x, new_y) in g.walls:
                symbol = '#'
            elif (new_x, new_y) == g.player:
                symbol = '$'
            elif (new_x, new_y) in g.explored:
                symbol = '.'
            else:
                symbol = ' '
            print("%%-%ds" % width % symbol, end="")
        print()


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def get():
    inkey = _Getch()
    while (1):
        k = inkey()
        if k != '': break
    if k == '\x1b[A':
        return "u"
    elif k == '\x1b[B':
        return "d"
    elif k == '\x1b[C':
        return "r"
    elif k == '\x1b[D':
        return "l"


def get_walls(g: MapGrid, pct=.25) -> list:
    out = []
    for i in range(int(g.height * g.width * pct) // 2):
        x = randint(1, g.width - 2)
        y = randint(1, g.height - 2)

        out.append((x, y))
        out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    return out


def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(.01)


def main():
    g = MapGrid(50, 50)
    # g.walls = get_walls(g)

    while g.player != g.goal:
        draw_grid(g)
        print('Col: {}, Row: {}'.format(*g.player))
        print(g.screens_down, g.screens_right)
        d = get()
        g.move_player(d)
        clear()
    print("You made it!")


if __name__ == '__main__':
    main()
