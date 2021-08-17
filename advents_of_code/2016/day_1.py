from dataclasses import dataclass, field

real =  "L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2"


inp1 = "R2, L3"
inp2 = "R2, R2, R2"
inp3 = "R5, L5, R5, R3"


@dataclass
class Coords:
    direction: int = 0
    x: int = 0
    y: int = 0
    visited: set = field(default_factory=set)
    location: tuple = None


    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def move(self, n):
        dx, dy = self.moves[self.direction]
        for _ in range(n):
            if (self.x, self.y) in self.visited and not self.location:
                self.location = (self.x, self.y)
            else:
                self.visited.add((self.x, self.y))

            self.y = self.y + dy
            self.x = self.x + dx

    def R(self):
        self.direction += 1
        if self.direction == 4:
            self.direction = 0

    def L(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3


def solver(inp):
    coords = Coords()
    for token in inp.split(', '):
        direction = token[0]
        distance = token[1:]
        getattr(coords, direction)()
        coords.move(int(distance))

    return abs(coords.location[0]) + abs(coords.location[1])


def test_1():
    assert solver(inp1) == 5

def test_2():
    assert solver(inp2) == 2

def test_3():
    assert solver(inp3) == 12

def test_main():
    assert solver(real) == 12