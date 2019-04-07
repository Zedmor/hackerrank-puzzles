import re
from collections import Counter
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

coords = [tuple(int(z) for z in re.findall('(\d*),\s(\d*)', i)[0]) for i in open('input-6.txt').readlines()]

# coords = [(1, 1),
#           (1, 6),
#           (8, 3),
#           (3, 4),
#           (5, 5),
#           (8, 9)]
#
# print(coords)

all_x, all_y = zip(*coords)
print(all_x, all_y)

def manhatten_distance(param, crd):
    return abs(crd[0] - param[0]) + abs(crd[1] - param[1])


def get_best_coordinate(x, y, coords):
    total_dist = 0
    for crd in coords:
        total_dist += manhatten_distance((x, y), crd)
    return total_dist

dots = []

colors = cm.rainbow(np.linspace(0, 1, len(coords)))
color_picker = dict(zip(coords, colors))

width = max(all_x) - min(all_x) + 1
height = max(all_y) - min(all_y) + 1
print(f'Height {height} width {width}')

distances = np.zeros((width, height), dtype=object)

total_size = 0

for x in range(min(all_x), max(all_x) + 1):
    for y in range(min(all_y), max(all_y) + 1):
        total_dist = get_best_coordinate(x, y, coords)
        distances[x - min(all_x), y - min(all_y)] = total_dist
        if total_dist < 10000:
            total_size += 1

print(total_size)


def get_forevers(minx, maxx, miny, maxy, coords):
    invalid_points = []
    for x in range(minx, maxx):
        invalid_points.append(get_best_coordinate(x, miny, coords))
        invalid_points.append(get_best_coordinate(x, maxy, coords))
    for y in range(miny, maxy):
        invalid_points.append(get_best_coordinate(minx, y, coords))
        invalid_points.append(get_best_coordinate(maxx, y, coords))
    return invalid_points

forever_points = get_forevers(min(all_x) - 1, max(all_x) + 1, min(all_y) - 1, max(all_y) + 1, coords)

print(distances.T)
print(forever_points)

counter = Counter(d for d in dots if d not in forever_points)

print(counter)


plt.scatter(*zip(*coords))
# for crd, target in distances.items():
#     plt.scatter(*crd, color=color_picker[target])

plt.gca().invert_yaxis()
plt.show()
