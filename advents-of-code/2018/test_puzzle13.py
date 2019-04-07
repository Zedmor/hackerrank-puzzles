import pytest
from puzzle13 import Grid, Cart
from puzzle_13_frames import frames

test_grid = """"
/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/
"""

test_grid_2 = """
++++
++++
+>++
++++
"""


@pytest.fixture(autouse=True)
def grid():
    grid = Grid(open('input-13-tst.txt').readlines())
    return grid

@pytest.fixture(autouse=True)
def big_grid():
    grid = Grid(open('input-13.txt').readlines())
    return grid

def test_move(grid):
    grid.move()
    print(grid)

def test_replace_track(grid):
    assert grid[0][2] == '>'
    grid.replace_track(2, 0, 'z')
    assert grid[0][2] == 'z'

def test_is_straight(grid):
    assert grid.carts[0].next_is_straight('-')
    assert not grid.carts[0].next_is_straight('|')

def split_frames(frames):
    buffer = []
    for line in frames:
        if line != '':
            buffer.append(line.rstrip())
        else:
            yield buffer
            buffer = []

def test_by_frames(grid):
    fr = frames.split('\n')
    fr = list(split_frames(fr))
    for n, move in enumerate(fr):
        move_repr = '\n'.join(move)
        if grid.__repr__() == move_repr:
            print('Move #{} is valid'.format(n))
        else:
            print('Move #{} is invalid'.format(n))
            print('\nTest #{}'.format(n))
            print(move_repr)
            print('Grid #{}'.format(n))
            print(grid)

            raise AssertionError
        try:
            grid.move()
        except Exception:
            pass

def test_run_big_grid(big_grid):
    while True:
        big_grid.print()
        big_grid.move()

def test_grid_2():
