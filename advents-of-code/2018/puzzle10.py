import re
from collections import namedtuple
from itertools import islice

import matplotlib.pyplot as plt
import numpy as np

Point = namedtuple('Point', ['x', 'y', 'dx', 'dy'])

points = []


def parse(line):
    values = re.findall('position=<(.*),(.*)> velocity=<(.*),(.*)>', line)
    point = Point(*map(int, values[0]))
    return point


with open('input-10.txt') as f:
    for line in f:
        points.append(parse(line))


def draw(points, i):
    xy = islice(zip(*points), 0, 2)
    x = list(islice(zip(*points), 0, 1))[0]
    y = list(islice(zip(*points), 1, 2))[0]
    plt.scatter(*xy, s=1)
    plt.legend([i])
    plt.gca().invert_yaxis()
    # plt.xticks(np.arange(min(x), max(x) + 1, 100.0))
    # plt.yticks(np.arange(min(y), max(y) + 1, 100.0))

    plt.show()



def move(points):
    new_points = []
    for p in points:
        new_points.append(Point(x=p.x + p.dx, y=p.y + p.dy, dx=p.dx, dy=p.dy))
    return new_points

def get_xrange(points):
    x = list(islice(zip(*points), 0, 1))[0]
    rng = max(x) - min(x)
    return rng

xrange = get_xrange(points)

for i in range(100000):
    if get_xrange(points) < 100:
        draw(points, i)
    else:
        xrange = get_xrange(points)
    points = move(points)
