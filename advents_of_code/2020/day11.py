from collections import namedtuple

g = """LLLLLLL.LLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLL.L.LLLLLLL.LLLLLL.LLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLLL.LLLL.LLL.LLLLLLLLLL.LLLLLLL.LLLLL.L.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL
.LLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LL.LLLLLLL.LLL.LL.LLLLLLLLLLL.LLL..LLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL..LLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.L.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL
LLLLL.L.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLL..LLL.LLLLLL.LLLLLL.LLLL.LLLL.L.LLLLLL
LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.L.LL.LLLL.LLLLLL..LLLLLL.LLLLLLLL..LLLLL.LLLLLLLL..LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL.LLLLL.L.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
.LLLLLL..LLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLL.LLL
..LLLL......L.L..L..L..L.....LL..L.....L.....LLL.L.L.LL...L.....L...LL..L......L...LL......L
LL.LLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL..LLLLLL.LLLL.LLL.LLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLL.LL.LLLLLL.LLLL.LLLLLLLL.LLLLLL..LL.LLLLL.LLLL..L.
LLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLLLLLL.L.LL.LLLLLLL.L.LLLL.LLLLLLLL.LLLLLL.L.LLLLLLLLLLLLLLLL
LLLLLLL.L.LLLLLL.LLLLLLLLL.LL.LLLLL.LLLLL..L.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LL
LLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLL..LLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLL..LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLL.LLLLLL.L.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.LLLLL..LLLLLLLLLL.LLL.LLLLLLLLLLLLLL.LLL.LLLLLLLLL.LLLLL.L.LLLL.LLLLLLLLLLL
.L......L.LL.L...L.....L..L..L...LL.L.......L.............LL.L......LL.L...LL.L...L.....LL..
LL.LLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLL.L.L.LLLLLLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLL.LL.LL.LLLLL.LLLL.L.LLLLL.LLLLLLLLLL.LLLLLLLLL..L.LLLLLLLLLLL.L.LLLLL.LLLLLLLLLLLLLLLL.L
LLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLL.L
.......LL...L.......LL...L.......LLL......L..L...L...L.....LL..L.L......L.LL.....LL.....L...
LLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLL.LL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLLLLLLLLL..LLLLLLLLLLLLL.LLLL.LL.LLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLL.LLLLLL.L.LLL.L.LLL.LLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLL
L.LLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLL..LLLLLL.LLLLLLLLL.LLLLLLLL
LL.LLLL.LLLLLLLL.LLLLLL.LLLLL.LL.LLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLL.LLLLLL.LL.LLLLLLLL
LLLLL.L.LLLLLLLL.LLLLLLLLLL.L.LLL.LLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL.LLLLL.LLLLL.L.LLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLL.LLLLLL.LL.LLL.LLLL
L..LL.........L....L....L..L.LL.....LL.L.LL...L........L...L...L...L.LLL..LL..LLLLL.L.......
LLLLLLL.LLLLLLLLLLLL.LL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLL.LLLLLLL.L..LLLLLLL
LLLLLLLL.LLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLL.LLLLLL.LLLL.L.LL.LLLLLLLL
.LLLLLL.LLLLLL.L.LLLLLL.LLLLL.LLLLLLL.L.LL.LLLLLLLLLLL.LLLLLLLLLLL.LLLLLL.LLLLLLLL..LLLLLLLL
LL.LLLL..LLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL..LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
L..LL..........L......L..L....L..L.L.LL.LLL..L.L.L.LLLL...L..L..L.L.L..LLLL.L.L...L..LL.....
LLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLL.LL.L.LLLLLLL.LLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLL.LL.LLLLL.LL.LLL.LLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLLL.LLLLLL.
LLLLLL.LLLLLLLLL.LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLL
LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLL.LLLL.LLL.LLLLLL.LLL.L.LLLLLLLLL.LL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLL.L.LLLLLL
LLLLLLLLLLLLL.LL.LLLLLL.LLL.L.LLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLL.LLL.LLLLLL.LLLLLL.LLLLLLLLLLL
.L.LLLL.L.LLL.L....L...LL.L.L..LL.L.LLLL.L..L..L.L.LL...LL..L.L.L...LL.L.......LL..LLL......
LLLLL.L..LLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LL.LLLL.LLLLLL.LLLLLL.L.LLLLLL.LLLLLLLLLLLL.LLLLL
LLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL..LLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLL
LLLLLLL.LLLLLLLL.LLLL.L.LLL.LLLLLLLLL.LLLL.LLLLLLL.L..LLL.LLLLLLL..LL.LLL.LLLLLLLLL.LLL.LLL.
LLLLLLL.LLLLLLLL.LLLLLL.L.LLLLLLLLLL..LLLLLLLLLLLL.L.LLLL.LLLLLLLL.LLLLLL.L.LLLL.LL.LLLL.LLL
LLLL.LLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLL.LLLLLL.LL.LLLLL.LLL.LL.LLLLLLLLLLLLLLLLLL
LL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLL.LLL.LLLL.LLLLLLLLLLLL.L.LLLLL.LL.LLLLLL.L.L.LLLLLLLLLLLLLL
LLLLLL.LLLLLL.LL.LLLLLLLLL.LLLLLLLLLL.LLLL.LL.LLLLLLLLLLL.LL.LLLLL.LLLLL.LLLLLLLLLL.LLLLLLLL
.LLL.......LL.LL....L..L.....LL.....L..L...LLL....L...L..LLL...L............LLLL.LL.......L.
LLLLL.L.LLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLL.LL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL
L.LLLLL...LLLLLLLLLLLLL.LLLLLLLLLLLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.L.L.LLLLLLLL.LLLLLLL.LLLL.LLLLL.L.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL
LLL.LLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLL.LLL.LLLLLL..LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL
L..L.LL...LLL.L...LLL....L.L.L.L.....LL..........LL...L.L.L.LLLL....L.....L....LLL......LLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.L.LLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLL..LLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLL.L.L.LL.LLLLLLLLLLL
LLLLLLLLLLLLLLLL.LLLL.L.LLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLLLLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLL.L
LLLLLLLL.LLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLL.LLL.LLL.LLLLLL.LLLLLLLL.LLLLLL.LLL.LLLLL.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL..LLLLLLLLLLLL.LLLL.L..L.LL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLL..LLLLLLLLLLLL.LLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLL.L.LLLLLLL.LLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLL..LLLLLLLL.LLLLLLLLLLLL.LLLLLL..LLLL.LLLL.LL.L.LLLL.LLLL.LLL.LLLLLL.LLLLLLLLLLLL.LLLLL
........LL..LL..L............L..L.L..L....L.......LL...L......L....LLL..L.L......LL..LL.L.L.
LLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLL..LLLL.LLLLLLL.LLL.LL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLL.LLLL
LLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLL.LLL.LLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLL..LLL.LLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLL.L.LLLLL.LL.LLLL.LLLL.L.LLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL..LLLL.LLLLLL.LLLLLLL.LLLLLL.LLLLLLLL.LLLLLLL.L.LLLLLLLL
LLLLLLL.LLLLL.LL.LLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLL.LLLL.LL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LL.LLLLLLLLLLLLL.LLLLLLLL
LLLL.L.L...L.......L..LL.LL.LL....LL..L.L.L......L...LLL..L.L.L...LLL...L.....L.LLLL........
.LLLLLL.L.LLLLLL.LLLLLLLLLLL..LLLLLLL.LLLL.LLLLLLL.LLLLLL.LLLLL.LLLLLLLLL.LLLL.LLLL.LLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL.
LLLLLLL.L.LLLLLLLLLLLLL.LLLLL.LLL.LLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLL.LL.L.LLLLLLLLLLLLLLLL
LLLLLLL.LLLLL.LL.LLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLL.LL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL
L.LLLLL.LLLLL.LLLLLLLLL.LLLLL..LLLLLL.LLLL.LLLLLLL.L.LLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLL.LL..
..L...L.L.......LL.LLL.LLL..L....L..L.L.L..L.L........L...L.LL.L.........LLLLL.L.LL.L...L.LL
LLLLLLL.LLLLL.LL.LLLLLL.LLLL..LLLLL.L.LL.LLLLLL.LL.LLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLL
LLLLLLL.L.LLLLLLLLLLLLL.LLLLL.LL.LLLLLLL.LLLLLLLLL.LLL.LL.LLLLLLLL.LLL.LL.LLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL..L.LLLLLLLLLLLL.LLLLLL.L.LLLLLL.LLLLLL.LLLLLLLLL.LLL.LLLL
.LLLLLL.LL.LL.LLLLLL.L..LLLLLLL.LLLLL.LLLL.LL.LL.L.LL.L.L.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLL.LLL.LLLLLLLLLLLLLLLLLL..LLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLL.LL.LL..LLLLLLLL.LLLLLLLLLLLLLLLL.LLL..LLL
LLLLLLLLL.LL.LLL.LLLLLLLLLLLLLLLLLLLL.LLL..LLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLL.LLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLL.L.LLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLL......LL...L...L..LL..L..L......L...L.L..L.........L.LL.LL..L..L.L......L..L........L..L.
LL.LLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL
LLLLLLLLLLLLLL.L.LLLLLLLLLLLL.LL.LLLL..LLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LL.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLLLL.L.LLLLLL.LLLLLLLL..LLLLL.LLLLLLLLL.LLLLLLLL
LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLL.LLL.LLLLLL.LL.LLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLL.LLLLLL.LLL.L.LLLLLLL.LLLLLLLLLLLL.LLLLLLLLL.LLL.L.LLLLLL.LLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLL.LL.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLL.LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLL.LLL.LLLLLLLLLLL.LLLLLLLLL.LLLLLLLL"""

# g = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

g = [list(m) for m in g.split('\n')]


class Coords(namedtuple('Coords', ['row', 'col'])):

    # @lru_cache(None)
    def __add__(self, other):
        return Coords(self.row + other[0], self.col + other[1])


def occupy(crd, g, occupied):
    return '#' not in list(adjastent(crd, g, occupied)) and g[crd.row][crd.col] == 'L'


def vacate(crd, g, occupied):
    return list(adjastent(crd, g, occupied)).count('#') >= 5


def cleanup(to_occupy, to_vacate, occupied):
    for crd in to_vacate:
        occupied.remove(crd)
    for crd in to_occupy:
        occupied.add(crd)


def adjastent(crd, g, occupied):

    d = {}

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if not (dx == dy == 0):
                d[(dx, dy)] = crd

    while d:
        key = next(iter(d))

        new_coord = d[key] + key

        if not (new_coord.row >= 0 and new_coord.col >= 0 and new_coord.row < len(g) and new_coord.col < len(g[0])):
            del d[key]
        elif new_coord in occupied:
            del d[key]
            yield '#'
        elif g[new_coord.row][new_coord.col] == 'L':
            del d[key]
        else:
            d[key] = new_coord


cnt = 0

occupied = set()

while True:
    to_occupy = []
    to_vacate = []

    for row_i, row in enumerate(g):
        for col_i, col in enumerate(row):
            crd = Coords(row_i, col_i)

            if crd not in occupied and occupy(crd, g, occupied):
                to_occupy.append(crd)
            if crd in occupied and vacate(crd, g, occupied):
                to_vacate.append(crd)
    cleanup(to_occupy, to_vacate, occupied)

    # for row_i, row in enumerate(g):
    #     for col_i, col in enumerate(row):
    #         if (row_i, col_i) in occupied:
    #             print('#', end='')
    #         else:
    #             print(col, end='')
    #     print()
    # print()

    if not to_vacate and not to_occupy:
        print(len(occupied))
        break
