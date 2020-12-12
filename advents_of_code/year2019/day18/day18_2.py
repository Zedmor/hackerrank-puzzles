from collections import defaultdict
from copy import copy
from functools import lru_cache
from pprint import pprint
from queue import Queue

from advents_of_code.year2019.day18.models import Coords

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Game:
    def __init__(self, m):
        self.m = m
        self.heros = []
        self.keys = 0
        # self.map = {} # map from key to coord

        for row_n, row in enumerate(m):
            for col_n, col in enumerate(row):
                self.resolve_state(col, Coords(row_n, col_n))

    def resolve_state(self, col, coord):
        if col == '@':
            self.heros.append(coord)

        if col.islower():
            self.keys += 1

    @lru_cache(None)
    def valid(self, c: Coords):
        if c.row < 0 or c.col < 0:
            return False
        if c.row > len(self.m) - 1 or c.col > len(self.m[0]) - 1:
            return False

        if self.m[c.row][c.col] == '#':
            return False

        return True

    def build_graph(self):
        best_results = defaultdict(lambda: float('inf'))

        paths = defaultdict(lambda: defaultdict(dict))

        for i, hero_coord in enumerate(self.heros):
            q = Queue()
            from_path = f'hero_{i}'
            visited = set()
            q.put((0, hero_coord, set(), from_path, visited))

            while not q.empty():

                depth, c, keys, from_path, visited_state = q.get()

                for d in directions:
                    if self.valid(c + d):
                        new_keys = set(keys)
                        cell = self.m[(c + d).row][(c + d).col]
                        if cell.isupper():
                            new_keys.add(cell.lower())

                        if cell.islower():
                            paths[from_path][frozenset(keys)][cell] = min(
                                depth + 1,
                                paths[from_path][frozenset(keys)].get(cell, float('inf')))
                            paths[cell][frozenset(keys)][from_path] = min(
                                depth + 1,
                                paths[cell][frozenset(keys)].get(from_path, float('inf')))
                            if (frozenset(keys), cell) not in visited:
                                visited.add((frozenset(keys), cell))
                                q.put((0, c + d, set(), cell, visited))

                            continue

                        new_state = (c + d, frozenset(new_keys), from_path)

                        if best_results[new_state] > depth + 1:
                            best_results[new_state] = depth + 1
                            q.put((depth + 1, c + d, new_keys, from_path, visited))

        return paths

    def solve(self):
        best_results = defaultdict(lambda: float('inf'))

        result = float('inf')

        g = self.build_graph()

        q = Queue()

        state = (0, [f'hero_{el}' for el in range(4)], frozenset())
        q.put(state)

        while not q.empty():

            depth, locations, keys = q.get()

            for bot in range(4):
                best_prices = defaultdict(lambda: float('inf'))

                for keyset in g[locations[bot]].keys():
                    if keys.issuperset(keyset):
                        for target, price in g[locations[bot]][keyset].items():
                            best_prices[target] = min(best_prices[target], price)

                for target, price in best_prices.items():
                    if not target.startswith('hero') and target not in keys and len(keys) == self.keys - 1:
                        result = min(result, depth + price)

                    new_locations = copy(locations)
                    new_locations[bot] = target
                    new_keys = set(keys)
                    if not target.startswith('hero'):
                        new_keys.add(target)
                    new_keys = frozenset(new_keys)

                    new_state = (tuple(new_locations), new_keys)

                    if best_results[new_state] > depth + price:
                        best_results[new_state] = depth + price
                        q.put((depth + price, new_locations, new_keys))

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
