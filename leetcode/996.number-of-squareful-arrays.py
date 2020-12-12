#
# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#
# https://leetcode.com/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (47.83%)
# Total Accepted:    7.9K
# Total Submissions: 16.6K
# Testcase Example:  '[1,17,8]'
#
# Given an array A of non-negative integers, the array is squareful if for
# every pair of adjacent elements, their sum is a perfect square.
#
# Return the number of permutations of A that are squareful.  Two permutations
# A1 and A2 differ if and only if there is some index i such that A1[i] !=
# A2[i].
#
#
#
# Example 1:
#
#
# Input: [1,17,8]
# Output: 2
# Explanation:
# [1,8,17] and [17,8,1] are the valid permutations.
#
#
# Example 2:
#
#
# Input: [2,2,2]
# Output: 1
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9
#
#
from collections import defaultdict

import numpy

perfect_squares = set()


def is_square(apositiveint):
    if apositiveint in perfect_squares:
        return True
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    perfect_squares.add(apositiveint)
    return True


def myDFS(trans_dict, start, length, paths, path=[], visited=None):
    if not visited:
        visited = {start}
    path = path + [start]
    if len(path) == length:
        paths.append(path)
    else:
        for node in trans_dict[start]:
            if node not in visited:
                myDFS(trans_dict, node, length, paths, path, visited.union({node}))


class Solution:
    def numSquarefulPerms(self, A) -> int:

        matrix = [[0 for y in range(len(A))] for x in range(len(A))]

        graph = defaultdict(set)

        for i, el_i in enumerate(A):
            for j, el_j in enumerate(A):
                if i != j and is_square(el_i + el_j):
                    perfect_squares.add(el_i + el_j)
                    graph[(el_i, i)].add((el_j, j))
                    # matrix[i][j] = 1

        # for row in matrix:
        #     print(row)

        paths = []
        # m = numpy.array(matrix)
        # for i in range(1, len(A)):
        #     m = m.dot(m)
        #     print(m)


        for a in graph:
            myDFS(graph, a, len(A), paths)

        for i, path in enumerate(paths):
            paths[i] = tuple(p[0] for p in path)

        paths = set(paths)
        print(paths)

        return len(paths)


# print(Solution().numSquarefulPerms([1,17,8,3]))
# print(Solution().numSquarefulPerms([2,2,2]))

print(Solution().numSquarefulPerms([2,2,2,2,23,2,2,2,2,2]))
