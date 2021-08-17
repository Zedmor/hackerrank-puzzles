import heapq
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from typing import List

"""
 The chips are prototypes and don't have normal radiation shielding, but they do have the ability 
 to generate an electromagnetic radiation shield when powered.
 
  Unfortunately, they can only be powered by their corresponding RTG. An RTG powering a microchip 
  is still dangerous to other microchips.
  
  if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, 
  the chip will be fried
  
  Its capacity rating means it can carry at most yourself and two RTGs or microchips in any 
  combination.
  
  As a security measure, the elevator will only function if it contains at least one RTG or 
  microchip.
  
  The elevator always stops on each floor to recharge, and this takes long enough that the items 
  within it and the items on that floor can irradiate each other. (You can prevent this if a 
  Microchip and its Generator end up on the same floor in this way, as they can be connected 
  while the elevator is recharging.)
"""


class ItemType(Enum):
    generator = "G"
    microchip = "M"

    def __lt__(self, other):
        self.value < other.value


def left_rotate_one(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp


def generate_generic_state(state, source_mats):
    new_state = state.clone()

    counter = 0
    mats = {}

    for room in new_state.rooms:
        for item in room:
            if item.mat not in mats:
                mats[item.mat] = counter
                counter += 1
            item.mat = source_mats[mats[item.mat]]
    for item in new_state.elevator:
        if item.mat not in mats:
            mats[item.mat] = counter
            counter += 1
        item.mat = source_mats[mats[item.mat]]
    return new_state, counter


@lru_cache(None)
def get_universal_hash(source_state):
    _, counter = generate_generic_state(source_state, [str(z) for z in range(1000)])
    mats = [str(z) for z in range(counter)]
    hashes = []
    for _ in mats:
        state, _ = generate_generic_state(source_state, mats)
        hashes.append(hash(state))
        left_rotate_one(mats)

    return min(hashes)



def iteratively_move_items_from_a_to_b(a: List, b: List, level=0):
    for i in range(len(a)):
        b.append(a.pop(i))
        yield list(a), list(b)
        if level < 2:
            yield from iteratively_move_items_from_a_to_b(list(a), list(b), level + 1)
        a.insert(i, b.pop(-1))


@dataclass
class Item:
    typ: ItemType
    mat: str

    def __hash__(self):
        return hash(f"{self.typ}_{self.mat}")


def check_level(level_content):
    generators = set()
    microchips = set()
    for item in level_content:
        if item.typ == ItemType.generator:
            generators.add(item.mat)
        else:
            microchips.add(item.mat)

    return not (len(generators) > 0 and len(microchips - generators) > 0)


class GameState:
    def __init__(self, rooms=None, floor=None, elevator=None):
        self.rooms = rooms if rooms else []
        self.level = floor if floor is not None else 0
        self.elevator = elevator if elevator else set()

    def clone(self):
        new_rooms = []
        for room in self.rooms:
            new_room = set()
            for item in room:
                new_room.add(Item(item.typ, item.mat))
            new_rooms.append(new_room)

        new_elevator = set()
        for item in self.elevator:
            new_elevator.add(Item(item.typ, item.mat))

        return GameState(rooms=new_rooms, floor=self.level, elevator=new_elevator)

    def hash_for_collection(self, coll):
        hash_collector = ''
        for item in sorted(coll, key=lambda i: (i.mat, i.typ)):
            hash_collector += '_' + str(hash(item))
        return str(hash(hash_collector))

    def __hash__(self):
        hash_collector = ''
        for room in self.rooms:
            hash_collector += self.hash_for_collection(room)
        hash_collector += self.hash_for_collection(self.elevator)
        result = hash(f"{hash(hash_collector)}_{str(self.level)}")
        return result

    def __lt__(self, other):
        self.heuristic_score() < other.heuristic_score()

    def __eq__(self, other):
        self.heuristic_score() == other.heuristic_score()

    def __repr__(self):
        string_collector = '\n'
        for i in range(3, -1, -1):
            string_collector += f'F{i + 1}'
            if self.level == i:
                string_collector += ' E'
                string_collector += ' ('
                string_collector += ', '.join([element.mat[0] + element.typ.value for element in self.elevator])
                string_collector += ') '
            else:
                string_collector += ' .  '
                
            for element in self.rooms[i]:
                string_collector += element.mat[0] + element.typ.value + ' '
            string_collector += '\n'
        return string_collector

    def locked_floor(self, i):
        return all([len(self.rooms[c]) == 0 for c in range(i + 1)])

    def heuristic_score(self):
        return -len(self.rooms[3])

    def solved(self):
        if (len(self.elevator) == 0 and self.level == 3 and all(
                [len(self.rooms[i]) == 0 for i in range(3)])):
            return True

    def valid(self):

        # If all rooms are clear and elevator on 4th floor this is correct state

        if self.solved():
            return True

        elevator_size_correct = 0 <= len(self.elevator) <= 2

        all_levels_correct = True

        for level in range(4):
            level_content = self.rooms[self.level]
            if self.level == level:
                level_content = level_content.union(self.elevator)
            all_levels_correct &= check_level(level_content)

        return all([elevator_size_correct, all_levels_correct])

    def new_states_generator(self):
        # Go up and down
        if 1 <= len(self.elevator) <= 2:
            if self.level < 3:
                new_state = self.clone()
                new_state.level += 1
                yield new_state, 1

            if self.level > 0:
                new_state = self.clone()
                new_state.level -= 1
                yield new_state, 1

        # Load each item in elevator

        new_state = self.clone()
        elevator = list(new_state.elevator)
        room = list(new_state.rooms[new_state.level])

        if not self.locked_floor(new_state.level):
            for new_elevator, new_room in iteratively_move_items_from_a_to_b(list(elevator), list(room)):

                constructed_state = self.clone()
                constructed_state.elevator = set(new_elevator)
                constructed_state.rooms[constructed_state.level] = set(new_room)
                yield constructed_state, 0

        for new_room, new_elevator in iteratively_move_items_from_a_to_b(list(room), list(elevator)):

            constructed_state = self.clone()
            constructed_state.elevator = set(new_elevator)
            constructed_state.rooms[constructed_state.level] = set(new_room)
            yield constructed_state, 0


def solver(state: GameState):
    counter = 0
    visited = defaultdict(lambda: float('inf'))
    queue = []
    heapq.heappush(queue, (0, state, [state.clone()]))
    best_solution = float('inf')
    while queue:
        length, state, _path = heapq.heappop(queue)
        counter += 1
        if length > best_solution:
            continue
        if visited[get_universal_hash(state)] < length:
            continue
        if state.solved():
            best_solution = min(best_solution, length)
            best_path = list(_path)
            print(best_solution)
        else:
            for new_state, cost in state.new_states_generator():
                if (new_state.valid() and
                        visited[get_universal_hash(new_state)] > cost + length and
                        length + cost < best_solution):
                    visited[get_universal_hash(new_state)] = cost + length
                    new_path = list(_path)
                    new_path.append(new_state)
                    heapq.heappush(queue, (length + cost, new_state, new_path))
    print(counter)
    return best_solution, best_path


def test_example():
    state = GameState(
        [
            {Item(ItemType.microchip, "HYD"), Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ]

        )
    cost, path = solver(state)
    for element in path:
        print(element)
    assert cost == 11


def test_real():
    state = GameState(
        [{Item(ItemType.generator, "prom"), Item(ItemType.microchip, "prom"),
          Item(ItemType.generator, "ele"), Item(ItemType.microchip, "ele"),
          Item(ItemType.generator, "dili"), Item(ItemType.microchip, "dili")},

         {Item(ItemType.generator, "cob"), Item(ItemType.generator, "cur"),
          Item(ItemType.generator, "ruth"),
          Item(ItemType.generator, "plut")},
         {Item(ItemType.microchip, "cob"), Item(ItemType.microchip, "cur"),
          Item(ItemType.microchip, "ruth"),
          Item(ItemType.microchip, "plut")},
         set()
         ]
        )

    assert solver(state) == 11


def test_valid_checker():

    state = GameState(
        [
            set(),
            set(),
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.microchip, "HYD"),}
            ],
        floor=3,
        elevator={Item(ItemType.generator, "LITH"), Item(ItemType.microchip, "LITH")}
        )

    assert not state.valid()


    state = GameState(
        [
            {Item(ItemType.microchip, "HYD"), Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=0,
        elevator=set()
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=0,
        elevator={Item(ItemType.microchip, "HYD"), }
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=1,
        elevator={Item(ItemType.microchip, "HYD"), }
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=2,
        elevator={Item(ItemType.microchip, "HYD"), }
        )
    assert not state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=3,
        elevator={Item(ItemType.microchip, "HYD"), }
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=1,
        elevator={Item(ItemType.microchip, "HYD"), }
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            set(),
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=1,
        elevator={Item(ItemType.microchip, "HYD"), Item(ItemType.generator, "HYD")}
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            set(),
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=2,
        elevator={Item(ItemType.microchip, "HYD"), Item(ItemType.generator, "HYD")}
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            set(),
            {Item(ItemType.generator, "LITH"), Item(ItemType.generator, "HYD")},
            set()
            ],
        floor=2,
        elevator={Item(ItemType.microchip, "HYD")}
        )
    assert state.valid()

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            set(),
            {Item(ItemType.generator, "LITH"), Item(ItemType.generator, "HYD")},
            set()
            ],
        floor=1,
        elevator={Item(ItemType.microchip, "HYD")}
        )
    assert state.valid()

    state = GameState(
        [
            set(),
            set(),
            set(),
            {Item(ItemType.microchip, "HYD"),
             Item(ItemType.generator, "LITH"),
             Item(ItemType.generator, "HYD"),
             Item(ItemType.microchip, "LITH")}
            ],
        floor=3,
        elevator=set()
        )
    assert state.valid()


def test_check_level():
    assert check_level({Item(ItemType.generator, "prom"), Item(ItemType.microchip, "prom")})
    assert not check_level({Item(ItemType.generator, "zed"), Item(ItemType.microchip, "prom")})
    assert check_level({Item(ItemType.generator, "zed"), Item(ItemType.microchip, "prom"),
                        Item(ItemType.microchip, "zed")})
    assert check_level({Item(ItemType.generator, "zed")})
    assert check_level(set())
    assert check_level({Item(ItemType.generator, "zed"), Item(ItemType.generator, "z"),
                        Item(ItemType.generator, "x")})

    assert check_level({Item(ItemType.microchip, "zed"), Item(ItemType.microchip, "z"),
                        Item(ItemType.microchip, "x")})


def test_item_mover():
    result = list(iteratively_move_items_from_a_to_b([1, 2, 3], []))

    assert result == [([2, 3], [1]),
         ([3], [1, 2]),
         ([], [1, 2, 3]),
         ([2], [1, 3]),
         ([], [1, 3, 2]),
         ([1, 3], [2]),
         ([3], [2, 1]),
         ([], [2, 1, 3]),
         ([1], [2, 3]),
         ([], [2, 3, 1]),
         ([1, 2], [3]),
         ([2], [3, 1]),
         ([], [3, 1, 2]),
         ([1], [3, 2]),
         ([], [3, 2, 1])]

    result = list(iteratively_move_items_from_a_to_b([1, 2], []))

    assert result == [([2], [1]), ([], [1, 2]), ([1], [2]), ([], [2, 1])]


def test_repr():
    state = GameState(
        [
            {Item(ItemType.microchip, "HYD"), Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ]

        )
    print(str(state))

    h = hash(state)

    state2 = GameState(
        [
            {Item(ItemType.microchip, "LITH"), Item(ItemType.microchip, "HYD"), },
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ]

        )

    assert hash(state2) == h


def test_problem_state():

    state = GameState(
        [
            {Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=1,
        elevator={Item(ItemType.microchip, "HYD"), }
        )
    print(state)
    assert state.valid()

    for sub_state in state.new_states_generator():
        print(sub_state)


def test_hash_generation():
    state = GameState(
        [
            {Item(ItemType.microchip, "HYD"), Item(ItemType.microchip, "LITH")},
            {Item(ItemType.generator, "HYD")},
            {Item(ItemType.generator, "LITH")},
            set()
            ],
        floor=0,
        elevator=set()
        )

    state2 = GameState(
        [
            {Item(ItemType.microchip, "LITH"), Item(ItemType.microchip, "HYD")},
            {Item(ItemType.generator, "LITH")},
            {Item(ItemType.generator, "HYD")},
            set()
            ],
        floor=0,
        elevator=set()
        )

    assert get_universal_hash(state) == get_universal_hash(state2)