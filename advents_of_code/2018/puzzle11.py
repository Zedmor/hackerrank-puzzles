from scipy.ndimage.filters import uniform_filter as unif2D

import numpy as np

SERIAL = 4842
# SERIAL = 18
grid = np.zeros([301, 301], dtype=int)


def get_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = int(float(power) / 100 % 10)
    power -= 5
    return power


for x in range(1, 301):
    for y in range(1, 301):
        power = get_power(x, y, SERIAL)
        grid[x, y] = power

max_sum = -float('inf')
best_x, best_y, best_size = 0, 0, 0

# s_gr = grid[33:36, 45:48].T
# print(s_gr)
# print(np.sum(s_gr))

# for size in range(1, 301):
#     for x in range(1, 301 - size):
#         for y in range(1, 301 - size):
#             subgrid = grid[x:x+size, y:y+size].T
#             s = np.sum(subgrid)
#             if s > max_sum:
#                 max_sum = s
#                 best_x, best_y, best_size = x, y, size



def largest_sum_pos_app1_mod1(a, n):
    idx = unif2D(a.astype(float), size=n, mode='constant').argmax()
    x, y = np.unravel_index(idx, a.shape)
    x, y = x - n // 2, y - n // 2
    return x, y

n = 16

max_sum, max_x, max_y, max_n = -float('inf'), 0, 0, 0
for n in range(1, 301):
    x, y = largest_sum_pos_app1_mod1(grid, n)
    s = np.sum(grid[x: x+n, y: y+n])
    if s > max_sum:
        max_sum = s
        max_x, max_y, max_n = x, y, n

print(max_x, max_y, max_n)
