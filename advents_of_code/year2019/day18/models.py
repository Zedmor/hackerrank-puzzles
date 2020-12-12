import re
from abc import ABC, abstractmethod
from collections import namedtuple, defaultdict
from functools import lru_cache
from queue import PriorityQueue
from typing import Dict, Optional, List

from scipy.spatial import distance


class Coords(namedtuple('Coords', ['row', 'col'])):

    @lru_cache(None)
    def __add__(self, other):
        return Coords(self.row + other[0], self.col + other[1])


@lru_cache(None)
def cached_euclidean(neighbour, goal):
    return distance.euclidean(neighbour, goal)


class Tile(ABC):
    repr = None

    @classmethod
    def build(cls, tag, **kwargs):
        for subclass in cls.__subclasses__():
            if re.match(subclass.repr, tag):
                return subclass(tag, **kwargs)

        raise ValueError('No suitable class for item')

    @abstractmethod
    def __init__(self, *args, **kwargs):
        self.coords = kwargs.get('coords')


class Obstacle(Tile):
    repr = '#'

    passable = False

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return '#'


class Door(Tile):
    repr = '[A-Z]'

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.opened = False
        self.tag = tag

    def __repr__(self):
        return self.tag


class Key(Tile):
    repr = '[a-z]'

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.door = tag

    def __repr__(self):
        return self.door


class Empty(Tile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    repr = '\.'

    def __repr__(self):
        return '.'


class Hero(Tile):
    repr = '@'

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.game = kwargs.get('game')
        self.keys = set()
        self.saved = Empty(self.coords)

    def __repr__(self):
        return f'@'

    def is_open_door(self, coords, keys=None):
        if not keys:
            keys = self.keys
        obj = self.game.state[coords]
        if isinstance(obj, Door):
            for key in keys:
                if str(key).upper() == str(obj):
                    return True
            return False
        else:
            return True

    def is_obstacle(self, coords):
        return isinstance(self.game.state[coords], Obstacle)

    def north(self):
        self.move(self.coords + N)

    def south(self):
        self.move(self.coords + S)

    def west(self):
        self.move(self.coords + W)

    def east(self):
        self.move(self.coords + E)

    @lru_cache(None)
    def can_move(self, new_coords, keys=None):
        if not keys:
            keys = self.keys
        return (new_coords in self.game.state
                and not self.is_obstacle(new_coords)
                and self.is_open_door(new_coords, keys))

    def move(self, new_coords):
        if self.can_move(new_coords):
            self.game.state[self.coords] = self.saved
            self.saved = self.game.state[new_coords]
            self.coords = new_coords
            self.game.state[new_coords] = self

    def pick_up_key(self):
        if isinstance(self.saved, Key):
            key = self.saved
            self.keys.add(key)
            self.saved = Empty(self.coords)
            self.game.keys.remove(key)

    def run(self):
        dp = defaultdict(lambda: (float('inf')))
        start_state = frozenset(self.game.keys)
        dp[(start_state, self.coords)] = 0
        queue = [(start_state, self.coords)]

        visited = set()

        while queue:
            item, coords = queue.pop()
            for key in item:
                try:
                    new_item = frozenset(item - {key})
                    if (new_item, key.coords) in visited:
                        continue
                    dp[(new_item, key.coords)] = min(dp[(item, coords)] + len(self.find_path(
                                                          coords,
                                                          key.coords,
                                                          frozenset(self.game.keys - item)
                                                      )), dp[(new_item, key.coords)])
                    queue.append((new_item, key.coords))
                    visited.add((new_item, key.coords))
                except KeyError:
                    continue

        return min([v for k, v in dp.items() if k[0] == frozenset()])

    @lru_cache(10000)
    def find_path(self, start, finish, keys):
        came_from, _ = self.a_star(start, finish, keys)
        return self.reconstruct_path(came_from, start, finish)[1:]

    def reconstruct_path(self, came_from: Dict[Coords, Coords],
                         start: Coords, goal: Coords) -> List[Coords]:
        current: Coords = goal
        path: List[Coords] = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  # optional
        path.reverse()  # optional
        return path

    @lru_cache(None)
    def a_star(self, start, goal, keys=None):
        if keys is None:
            keys = self.keys

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from: Dict[Coords, Optional[Coords]] = {}
        cost_so_far: Dict[Coords, float] = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current: Coords = frontier.get()

            if current == goal:
                break

            for neighbour in self.neighbors(current, keys):
                new_cost = cost_so_far[current] + 1
                if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost + cached_euclidean(neighbour, goal)
                    frontier.put(neighbour, priority)
                    came_from[neighbour] = current

        return came_from, cost_so_far

    @lru_cache()
    def neighbors(self, coord: Coords, keys=None):
        result = []
        if keys is None:
            keys = self.keys
        for direction in (N, E, S, W):
            if self.can_move(coord + direction, keys):
                result.append(coord + direction)
        return result
