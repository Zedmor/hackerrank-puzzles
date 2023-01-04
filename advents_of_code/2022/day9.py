import math


class State:
    
    directions = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
        }
    
    def __init__(self):
        self.visited = set()
        self.rope = [[0, 0] for _ in range(10)]
        self.visited.add(tuple(self.rope[-1]))
        
    def go(self, direction, distance):
        distance = int(distance)
        while distance > 0:
            distance -= 1
            for axis in (0, 1):
                self.rope[0][axis] += self.directions[direction][axis]
            for head, tail in zip(self.rope, self.rope[1:]):
                if not self.head_tail_touching(head, tail):
                    self.move_tail_to_head(head, tail)
            self.visited.add(tuple(tail))
                # self.print_state()

    def head_tail_touching(self, head, tail):
        return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

    def move_tail_to_head(self, head, tail):
        dx = head[1] - tail[1]
        dy = head[0] - tail[0]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        dir_ = [0, 0]
        if dx > 0 and dy > 0:
            # move diagonally down and to the right
            dir_ = [1, 1]
        elif dx < 0 and dy < 0:
            dir_ = [-1, -1]
        elif dx > 0 and dy < 0:
            dir_ = [-1, 1]
            # move diagonally up and to the right
        elif dx < 0 and dy > 0:
            # move diagonally down and to the left
            dir_ = [1, -1]
        elif dx == 0 and dy > 0:
            # move down
            dir_ = [1, 0]
        elif dx == 0 and dy < 0:
            dir_ = [-1, 0]
            # move up
        elif dx > 0 and dy == 0:
            dir_ = [0, 1]
            # move right
        elif dx < 0 and dy == 0:
            dir_ = [0, -1]
            # move left

        tail[0] += dir_[0]
        tail[1] += dir_[1]

    def print_state(self):
        print('\n============================\n')
        for row in range(-10, 10):
            print()
            for col in range(-10, 10):
                if tail == [row, col]:
                    print('T', end='')
                elif head == [row, col]:
                    print('H', end='')
                elif [row, col] == [0, 0]:
                    print('s', end='')
                else:
                    print('.', end='')



def main():
    state = State()
    with open("day9.txt") as commands:
        for command in commands:
            direction, distance = command.strip().split(" ")
            state.go(direction, distance)
    return len(state.visited)


def test_main():
    assert main() == 13