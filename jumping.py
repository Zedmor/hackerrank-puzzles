#!/bin/python3

import os


# Complete the jumpingOnClouds function below.
from collections import defaultdict


def find_shortest_path(graph, start, end, path=None):
    if not path:
        path = []
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def create_graph(clouds):
    graph = defaultdict(list)
    for i in range(len(clouds)):
        try:
            if not clouds[i + 1]:
                graph[i].append(i + 1)
            if not clouds[i + 2]:
                graph[i].append(i + 2)
        except IndexError:
            pass
    return graph


def jumpingOnClouds(clouds):
    """
    >>> jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
    4
    """
    graph = create_graph(clouds)
    return len(find_shortest_path(graph, 0, len(clouds) - 1)) - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
