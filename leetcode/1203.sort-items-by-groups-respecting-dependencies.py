#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
#
# algorithms
# Hard (48.62%)
# Total Accepted:    7.4K
# Total Submissions: 15.2K
# Testcase Example:  '8\n2\n[-1,-1,1,0,0,1,0,-1]\n[[],[6],[5],[6],[3,6],[],[],[]]'
#
# There are n items each belonging to zero or one of m groups where group[i] is
# the group that the i-th item belongs to and it's equal to -1 if the i-th item
# belongs to no group. The items and the groups are zero indexed. A group can
# have no item belonging to it.
#
# Return a sorted list of the items such that:
#
#
# The items that belong to the same group are next to each other in the sorted
# list.
# There are some relations between these items where beforeItems[i] is a list
# containing all the items that should come before the i-th item in the sorted
# array (to the left of the i-th item).
#
#
# Return any solution if there is more than one solution and return an empty
# list if there is no solution.
#
#
# Example 1:
#
#
#
#
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
#
#
# Example 2:
#
#
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6
# in the sorted list.
#
#
#
# Constraints:
#
#
# 1 <= m <= n <= 3*10^4
# group.length == beforeItems.length == n
# -1 <= group[i] <= m-1
# 0 <= beforeItems[i].length <= n-1
# 0 <= beforeItems[i][j] <= n-1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.
#
#
#
from collections import defaultdict
from copy import copy
from functools import cmp_to_key
from typing import List

cache = {}


def cached_and_validated(comp):
    def wrapped(obj1, obj2, before=None):
        if (obj1, obj2) in cache and (obj2, obj1) in cache:
            if cache[(obj1, obj2)] != - cache[(obj2, obj1)]:
                raise Exception('Incompatible result')

        if (obj1, obj2) in cache:
            return cache[(obj1, obj2)]
        if (obj2, obj1) in cache:
            return -cache[(obj2, obj1)]

        result = comp(obj1, obj2, before)

        cache[(obj1, obj2)] = result

        return result

    return wrapped


@cached_and_validated
def comparator(obj1, obj2, before=None):
    """
    >>> comparator(1, 2)
    -1

    >>> comparator(2, 1)
    1

    >>> comparator((1,2,3), 4)
    -1

    >>> comparator((1,2,3), 0)
    1

    >>> comparator(0, 0)
    0

    >>> comparator(6, 3, [[],[6],[5],[6],[3],[],[4],[]])
    -1

    >>> comparator(3, 4, [[],[6],[5],[6],[3],[],[4],[]])
    -1

    >>> comparator(6, 4, [[],[6],[5],[6],[3,6],[],[],[]])
    -1


    :param obj1:
    :param obj2:
    :param before:
    :return:
    """

    if (obj1, obj2) in cache:
        return cache[(obj1, obj2)]

    if (obj2, obj1) in cache:
        return -cache[(obj2, obj1)]

    if not before:
        before = [[] for i in range(50)]
    if isinstance(obj1, tuple):
        results = [comparator(i, obj2, before) for i in obj1]
        results = [r for r in results if r in (-1, 1)]
        if not results:
            return 0
        return results[0]
    if isinstance(obj2, tuple):
        results = [comparator(obj1, i, before) for i in obj2]
        results = [r for r in results if r in (-1, 1)]
        if not results:
            return 0
        return results[0]

    if obj1 in before[obj2]:
        return -1
    if obj2 in before[obj1]:
        return 1

    if obj1 < obj2:
        return -1
    if obj1 > obj2:
        return 1
    return 0


def bubbleSort(alist, comp):
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            if comp(alist[i], alist[j]) == 1:
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp


def cycle_detected(beforeItems):
    """
    >>> cycle_detected([[],[6],[5],[6],[3,6],[],[],[]])
    False

    >>> cycle_detected([[],[6],[5],[6],[3],[],[4],[]])
    True

    :param beforeItems:
    :return:
    """

    def recur(i, visited=None):
        if not visited:
            visited = set()

        if i in visited:
            return True

        return any([recur(v, visited.union({i})) for v in beforeItems[i]])

    return any([recur(i) for i in range(len(beforeItems))])


class Solution:
    """
    >>> Solution().sortItems(n = 5, m = 5, group = [2,0,-1,3,0], beforeItems = [[2,1,3],[2,4],[],[],[]])
    [6, 3, 4, 1, 5, 2, 0, 7]

    >>> Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]])
    [6, 3, 4, 1, 5, 2, 0, 7]

    >>> Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]])
    []

    """

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        if cycle_detected(beforeItems):
            return []

        source = []
        groups = defaultdict(list)

        cmp = lambda a, b: comparator(a, b, beforeItems)

        for i, g in enumerate(group):
            if g == -1:
                source.append(i)
                continue
            groups[g].append(i)
        for g in groups.values():
            new_g = copy(g)
            bubbleSort(new_g, cmp)
            source.append(tuple(new_g))
        try:
            bubbleSort(source, cmp)
        except Exception:
            return []

        new_source = []

        for e in source:
            if isinstance(e, tuple):
                new_source += list(e)
            else:
                new_source.append(e)

        return new_source
