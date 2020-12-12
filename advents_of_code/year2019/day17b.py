import os
import sys
import time
from collections import Counter, defaultdict
from copy import copy
from heapq import heappush, heappop
from pprint import pprint

sys.setrecursionlimit(100000)

from advents_of_code.common import Computer

with open('advents_of_code/2019/day17.txt') as data:
    program = list(map(int, data.read().split(',')))

c = Computer(program, wait_for_input=True)

while not c.terminated:
    c.run_software()

maze = ''.join([chr(code) for code in c.outputs]).split()


clear = lambda: os.system('clear') #on Linux System
clear()


def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if maze[i][j] in ('#', '^')}
    for row, col in graph.keys():
        if row < height - 1 and maze[row + 1][col] in ('#', '^'):
            graph[(row, col)].append((row + 1, col))
            graph[(row + 1, col)].append((row, col))
        if col < width - 1 and maze[row][col + 1] in ('#', '^'):
            graph[(row, col)].append((row, col + 1))
            graph[(row, col + 1)].append((row, col))
    return graph

graph = maze2graph(maze)

def get_scaffoldings(chars):
    for y, row in enumerate(chars):
        for x, col in enumerate(row):
            try:
                if (chars[y][x] == '#'
                        and chars[y - 1][x] == '#'
                        and chars[y + 1][x] == '#'
                        and chars[y][x - 1] == '#'
                        and chars[y][x + 1] == '#'):
                    yield (y, x)
            except:
                pass

robot = (18, 12)

scaffoldings = set(get_scaffoldings(maze))

# print(scaffoldings)


def find_paths(graph, cursor, visited=None, path=None, where_from=None):
    if not visited:
        visited = Counter()

    if not path:
        path = []

    visited[cursor] += 1
    path = path + [cursor]

    if set(graph[cursor]).issubset(set(visited.keys())):
        if set(visited.keys()) == set(graph.keys()):
            # print('Hit a dead end, visited all nodes')
            # print('Path {}'.format(path))
            return path

    for neigbour in graph[cursor]:
        if (visited[neigbour] < 1 or (visited[neigbour] < 2 and neigbour in scaffoldings)) and where_from != neigbour:
            res = find_paths(graph, neigbour, copy(visited), copy(path), where_from=cursor)
            if res:
                return res


path = find_paths(graph, robot)

print(path)

def reduce_path(path):
    steps = []

    directions = {(0, -1): 'E', (0, 1): 'W', (-1, 0): 'S', (1, 0): 'N'}

    change_directions = {
        ('N', 'E'): 'R',
        ('N', 'W'): 'L',
        ('S', 'E'): 'L',
        ('S', 'W'): 'R',
        ('W', 'N'): 'R',
        ('W', 'S'): 'L',
        ('E', 'N'): 'L',
        ('E', 'S'): 'R',
        ('E', 'W'): 'RR',
        ('S', 'N'): 'RR',
        ('N', 'S'): 'RR'
    }

    current_direction = 'N'

    cursor = path.pop(0)
    while path:
        dest = path.pop(0)
        direction = directions[tuple(x-y for x, y in zip(cursor, dest))]
        if direction == current_direction:
            steps.append('1')
        else:
            steps.append(change_directions[(current_direction, direction)])
            steps.append('1')
            current_direction = direction
        cursor = dest

    return steps

# print(global_path)
reduced_path = reduce_path(path)
print(''.join(reduced_path))


def find_sublists(reduced_path, min_len=0, min_usage=0):
    # store all the sublists
    sublist = defaultdict(list)

    # first loop
    for i in range(len(reduced_path) + 1):
        # second loop
        for j in range(i + 2, len(reduced_path) + 1):
            # slice the subarray
            sub = reduced_path[i:j]
            if sub[0] in ('R', 'L') and len(sub) >= min_len:
                sublist[tuple(sub)].append(i)

    sublist = {k: v for k,v in sublist.items() if len(v) >= min_usage}

    final_list = defaultdict(tuple)

    for k, v in sublist.items():
        index_pointers = tuple(v)
        if len(final_list[index_pointers]) < len(k):
            final_list[index_pointers] = k

    for pointer in copy(list(final_list.keys())):
        for pointer2 in copy(list(final_list.keys())):
            if set(pointer2).issuperset(pointer) and len(pointer2) > len(pointer):
                del final_list[pointer]

    return final_list


sublists = find_sublists(reduced_path, 14, min_usage=3)

print(sublists)

for name, (indexes, subroutine) in zip(['A', 'B', 'C', 'D'], sublists.items()):
    print(name, indexes, subroutine)
    for index in indexes:
        for i in range(len(subroutine)):
            reduced_path[i + index] = name

print(reduced_path)
