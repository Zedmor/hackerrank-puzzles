from copy import deepcopy

from advents_of_code.common import Computer

with open('day15.txt') as data:
    program = list(map(int, data.read().split(',')))

c = Computer(program, wait_for_input=True)

grid = [[0] * 50 for i in range(50)]


def comp_io(inp, computer):
    computer.inputs.append(inp)
    computer.run_software()
    return computer.outputs.pop()


def search(x, y, direction=None, computer=None):
    print('visiting %d,%d' % (x, y))

    if grid[y][x] == 2:
        print('found at %d,%d' % (x, y))
        return True
    elif grid[y][x] == 1:
        print('wall at %d,%d' % (x, y))
        return False
    elif grid[y][x] == 3:
        print('visited at %d,%d' % (x, y))
        return False

    if direction:
        res = comp_io(direction, computer)
        if res == 0:
            grid[y][x] = 1
            return False
        if res == 2:
            grid[y][x] = 2
            print('found at %d,%d' % (x, y))
            return False

    # mark as visited
    grid[y][x] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid) - 1 and search(x + 1, y, direction=4, computer=deepcopy(computer)))
            or (y > 0 and search(x, y - 1, direction=1, computer=deepcopy(computer)))
            or (x > 0 and search(x - 1, y, direction=3, computer=deepcopy(computer)))
            or (y < len(grid) - 1 and search(x, y + 1, direction=2, computer=deepcopy(computer)))):
        return True

    return False


search(25, 25, computer=c)
for line in grid:
    print(line)
