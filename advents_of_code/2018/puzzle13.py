import os
from collections import namedtuple

from collections import defaultdict
from typing import List, Tuple, Dict


class Newcart:
    def __init__(self, pos: complex, di: complex):
        self.position = pos
        self.direction = di
        self.cross_mod = 0
        self.dead = False

    def __repr__(self):
        return f"Direction: {self.direction} Position: {self.position}"


def setup(input_file_lines: List[str]) -> Tuple[Dict[complex, str], List[Newcart]]:
    tracks = defaultdict(lambda: "")  # only stores important tracks: \ / +
    carts = []
    for y, line in enumerate(input_file_lines):
        for x, char in enumerate(line):
            if char == "\n":
                continue
            if char in "<v>^":
                direction = {
                    "<": -1,
                    "v": +1j,
                    ">": +1,
                    "^": -1j,
                }[char]
                carts.append(Newcart(x + y * 1j, direction))  # location, direction, crossings
                part = {
                    "<": "-",
                    "v": "|",
                    ">": "-",
                    "^": "|",
                }[char]
            else:
                part = char
            if part in "\\/+":
                tracks[(x + y * 1j)] = part
    return tracks, carts


def turn_cart(cart: Newcart, part: str):
    """This space uses a downwards-facing Y axis, which means all calculations
    must flip their imaginary part. For example, rotation to the left
    (counterclockwise) would be multiplying by -1j instead of by +1j."""
    if not part:  # empty track is impossible, and | or - don't matter
        return
    if part == "\\":
        if cart.direction.real == 0:
            cart.direction *= -1j  # ⮡ ⮢
        else:
            cart.direction *= +1j  # ⮧ ⮤
    if part == "/":
        if cart.direction.real == 0:
            cart.direction *= +1j  # ⮣ ⮠
        else:
            cart.direction *= -1j  # ⮥ ⮦
    if part == "+":
        cart.direction *= -1j * 1j ** cart.cross_mod  # rotate left, forward, or right
        cart.cross_mod = (cart.cross_mod + 1) % 3


def solve_a(input_file_lines: List[str]) -> str:
    tracks, carts = setup(input_file_lines)
    while True:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            cart.position += cart.direction
            if any(c2.position == cart.position for c2i, c2 in enumerate(carts) if c2i != ci):
                return str(int(cart.position.real)) + "," + str(int(cart.position.imag))
                # 14, 42
            part = tracks[cart.position]
            turn_cart(cart, part)


def solve_b(input_file_lines: List[str]) -> str:
    tracks, carts = setup(input_file_lines)
    while len(carts) > 1:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            if cart.dead:
                continue
            cart.position += cart.direction
            for ci2, cart2 in enumerate(carts):
                if ci != ci2 and cart.position == cart2.position and not cart2.dead:
                    cart.dead = True
                    cart2.dead = True
                    break
            if cart.dead:
                continue
            part = tracks[cart.position]
            turn_cart(cart, part)
        carts = [c for c in carts if not c.dead]
    if not carts:
        return "ERROR: there's an even number of carts, there's isn't 1 cart left at the end!"
    cart = carts[0]
    return str(int(cart.position.real)) + "," + str(int(cart.position.imag))
    # 8,7

print(solve_b(open('input-13.txt').readlines()))


class Cart:
    moves = {'l': 's', 's': 'r', 'r': 'l'}

    def __repr__(self):
        return f'({self.orientation}, x: {self.x}, y: {self.y}, next turn: {self.next_turn})'

    def __init__(self, x, y, orientation, stash):
        self.next_turn = 'l'
        self.orientation = orientation
        self.x = x
        self.y = y
        self.stash = stash

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def __eq__(self, other):
        return (self.y, self.x) == (other.y, other.x)

    def move(self, grid):
        next_coords = grid.get_next_coords(self.x, self.y, self.orientation)
        if next_coords:
            next_spot = grid.get_next_spot(next_coords)
            self.move_cart(next_spot, next_coords, grid)

    def move_cart(self, next_spot, next_coords, grid):
        self.put_back_stashed_track(grid)
        old_track = grid[next_coords.y][next_coords.x]
        new_cart = self.make_new_cart(next_spot)
        if new_cart:
            self.orientation = new_cart
            grid.replace_track(next_coords.x, next_coords.y, new_cart)
            grid.replace_track(self.x, self.y, self.stash)
            self.stash = old_track
            self.x, self.y = next_coords

    def next_is_straight(self, next_spot):
        spot_orientation_lookup = {
            '-': ['<', '>'],
            '|': ['v', '^']

        }
        return next_spot in spot_orientation_lookup and self.orientation in spot_orientation_lookup[next_spot]

    def put_back_stashed_track(self, grid):
        grid[self.y][self.x] = self.stash

    def make_new_cart(self, next_spot):
        if self.simple_straight(next_spot):
            return self.orientation
        if self.natural_turn(next_spot):
            return self.natural_turn(next_spot)
        if self.crossroads(next_spot):
            move = self.crossroads(next_spot)
            self.next_turn = self.moves[self.next_turn]
            return move

    def simple_straight(self, next_spot):
        return (self.stash == next_spot and self.stash != '+') or (self.stash == '+' and next_spot in ('|', '-'))

    def natural_turn(self, next_spot):
        end_turns = {
            # ('>', '\\', '|'): 'v',
            # ('>', '/', '|'): '^',
            # ('<', '\\', '|'): '^',
            ('<', '/', '|'): 'v',
            ('<', '/', '-'): '<',
            # ('v', '//', '-'): '<',
            ('v', '\\', '|'): 'v',
            ('v', '\\', '+'): 'v',
            ('v', '/', '+'): 'v',
            ('^', '/', '|'): '^',
            ('^', '/', '+'): '^',
            ('^', '\\', '+'): '^',
            # ('^', '//', '-'): '>'
        }

        start_turns = {
            ('>', '\\'): 'v',
            ('>', '/'): '^',
            ('<', '/'): 'v',
            ('<', '\\'): '^',
            ('^', '\\'): '<',
            ('^', '/'): '>',
            ('v', '\\'): '>',
            ('v', '/'): '<',

        }
        move = (self.orientation, self.stash, next_spot)
        if move in end_turns:
            return end_turns[move]
        if (self.orientation, next_spot) in start_turns:
            return start_turns[(self.orientation, next_spot)]


    def crossroads(self, next_spot):
        right_rotate = {
            '>' : 'v',
            'v' : '<',
            '<' : '^',
            '^' : '>'
        }
        left_rotate = {v: k for k, v in right_rotate.items()}

        rotate = {'l': left_rotate,
                  'r': right_rotate}

        if self.next_turn == 's':
            return self.orientation
        return rotate[self.next_turn][self.orientation]





Coords = namedtuple('Coords', ['x', 'y'])


class Grid(list):
    orientation_offsets = {'v': (0, 1), '^': (0, -1), '>': (1, 0), '<': (-1, 0)}

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self])

    def __init__(self, string_with_newlines):
        super().__init__(list(map(lambda s: list(s.rstrip()), string_with_newlines)))

        self.carts = []

        for i in range(len(self)):
            for j in range(len(self[i])):
                el = self[i][j]
                if el in ['<', '>', 'v', '^']:
                    self.carts.append(Cart(j, i, el, self.make_stash(el)))

    def print(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.__repr__())

    def find_collision(self):
        return 1, 1

    def get_next_coords(self, x, y, orientation):
        try:
            return Coords(x + self.orientation_offsets[orientation][0], y + self.orientation_offsets[orientation][1])
        except IndexError:
            return None

    def get_next_spot(self, next_coords):
        return self[next_coords.y][next_coords.x]

    def replace_track(self, x, y, new_current):
        self[y][x] = new_current

    def move(self):
        self.carts.sort()
        for cart in self.carts:
            cart.move(self)
            try:
                x, y = self.collision(cart)
                self[y][x] = 'X'
                print(f'Collision in x: {x}, y:{y}')
                raise Exception
            except TypeError:
                pass

    def make_stash(self, el):
        stash_lookup = {'v': '|', '>': '-', '^': '|', '<': '-'}
        return stash_lookup[el]

    def collision(self, cart):
        for other_cart in self.carts:
            if cart.x == other_cart.x and cart.y == other_cart.y and cart is not other_cart:
                return cart.x, cart.y
        return False

def new_grid_move(carts, tracks):
    carts.sort(key=lambda c: (c.position.imag, c.position.real))
    for ci, cart in enumerate(carts):
        cart.position += cart.direction
        if any(c2.position == cart.position for c2i, c2 in enumerate(carts) if c2i != ci):
            return str(int(cart.position.real)) + "," + str(int(cart.position.imag))
            # 14, 42
        part = tracks[cart.position]
        turn_cart(cart, part)

def check_equality(grid, carts):
    for i, (cart1, cart2) in enumerate(zip(grid.carts, carts)):
        if complex(cart1.x, cart1.y) != cart2.position:
            print("Cart # {} defective".format(i))
            print(cart1)
            print(cart2.position)
            return False
    return True

if __name__ == '__main__':
    grid_content = open('input-13.txt').readlines()
    tracks, carts = setup(grid_content)
    grid = Grid(grid_content)

    cnt = 0
    while True:
        # grid.print()
        grid.move()
        new_grid_move(carts, tracks)
        if not check_equality(grid, carts):
            print(grid)
            print(cnt)
            input('Move: {}'.format(cnt))

        # if cnt > 27:
        # input('Move: {}'.format(cnt))
        cnt += 1
