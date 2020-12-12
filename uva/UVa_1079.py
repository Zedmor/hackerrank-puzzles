import random
from copy import copy
from itertools import permutations


def min_interval(pointers):
    return min([abs(pointers[i+1] - pointers[i]) for i in range(len(pointers) - 1)])

def solution(arg: list) -> str:
    planes = [tuple(map(int, i.split(' '))) for i in arg]
    n_planes = int(planes.pop(0)[0])
    results = []

    for order in permutations(range(len(planes))):
        r = max([i[1] for i in planes]) - min(i[0] for i in planes)
        l = 0

        while abs(r - l) > 1/120:
            mid = (r + l) / 2.0
            landing_times = []
            for i, plane in enumerate(order):
                if i == 0:
                    landing_times.append(planes[plane][0])
                else:
                    target = landing_times[i - 1] + mid
                    if target > planes[plane][1]:
                        r = mid
                        break
                    landing_times.append(max(planes[plane][0], target))
            else:
                if landing_times[-1] >= planes[plane][0]:
                    l = mid
        results.append(l)
    best_result = round(max(results) * 60)

    return f'{int(best_result) // 60}:{int(best_result % 60):02}'





