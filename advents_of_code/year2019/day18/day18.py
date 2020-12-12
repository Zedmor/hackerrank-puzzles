from collections import defaultdict
from copy import copy
from functools import lru_cache
from queue import Queue, PriorityQueue

from advents_of_code.year2019.day18.models import Coords

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Game:
    def __init__(self, m):
        self.m = m
        self.heros = []
        self.keys = 0

        for row_n, row in enumerate(m):
            for col_n, col in enumerate(row):
                self.resolve_state(col, Coords(row_n, col_n))

    def resolve_state(self, col, coord):
        if col == '@':
            self.heros.append(coord)

        if col.islower():
            self.keys += 1

    @lru_cache(None)
    def valid(self, c: Coords, keys):
        if c.row < 0 or c.col < 0:
            return False
        if c.row > len(self.m) - 1 or c.col > len(self.m[0]) - 1:
            return False

        cell = self.m[c.row][c.col]
        if cell == '#':
            return False
        if cell.isupper() and cell.lower() not in keys:
            return False

        return True

    def solve(self):

        best_results = defaultdict(lambda: float('inf'))

        # key: start, finish, keys NEEDED, value: steps taken (updated when we have shorter path
        paths = {}

        result = float('inf')

        q = PriorityQueue()

        q.put((0, self.heros, set()))

        while not q.empty():

            depth, all_coords, keys = q.get()

            for i, c in enumerate(all_coords):
                for d in directions:
                    if self.valid(c + d, frozenset(keys)):
                        new_keys = set(keys)
                        if self.m[(c + d).row][(c + d).col].islower():
                            new_keys.add(self.m[(c + d).row][(c + d).col])
                            if len(new_keys) == self.keys:
                                result = min(result, depth + 1)
                                continue

                        new_all_coords = copy(all_coords)
                        new_all_coords[i] = c + d

                        new_state = (tuple(new_all_coords), frozenset(keys))

                        if best_results[new_state] > depth:
                            best_results[new_state] = depth
                            q.put((depth + 1, new_all_coords, new_keys))

        return result


def get_vault():
    with open('day18.txt') as f:
        lab = f.read().splitlines()

    return lab


def main():
    vault = get_vault()
    game = Game(vault)
    print(game.solve())


if __name__ == '__main__':
    main()
