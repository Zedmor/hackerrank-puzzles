#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (72.74%)
# Total Accepted:    45.4K
# Total Submissions: 60.2K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# On a 2-dimensionalgrid, there are 4 types of squares:
#
#
# 1 represents the starting square. There is exactly one starting square.
# 2 represents the ending square. There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
#
#
# Return the number of 4-directional walksfrom the starting square to the
# ending square, that walk over every non-obstacle squareexactly once.
#
#
#
#
# Example 1:
#
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
#
# Example 2:
#
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#
# Example 3:
#
#
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation:
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= grid.length * grid[0].length <= 20
#
#
from collections import namedtuple
from copy import deepcopy
from typing import List


class Solution:
    """
    >>> Solution().uniquePathsIII([[0,1],[2,0]])
    0

    >>> Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
    4

    >>> Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    2
    """
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        Coord = namedtuple('Coord', ['x', 'y'])

        m = len(grid[0])  # width
        n = len(grid)  # height

        def tuple_sum(coord, offset):
            return Coord(*(sum(x) for x in zip(coord, offset)))

        all_visitable_squares = 0

        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == 1:
                    start = Coord(x, y)
                    all_visitable_squares += 1
                if col == 2:
                    finish = Coord(x, y)
                    all_visitable_squares += 1
                if col == 0:
                    all_visitable_squares += 1

        possible_solutions = set()

        def recur(visited, coord, path):
            # print(coord, visited, path)
            if coord == finish:
                if len(visited) >= all_visitable_squares:
                    possible_solutions.add(tuple(path))
                else:
                    return False

            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for offset in offsets:
                new_coord = tuple_sum(coord, offset)
                if 0 <= new_coord.x <= m - 1 and 0 <= new_coord.y <= n - 1:
                    if grid[new_coord.y][new_coord.x] != -1 and new_coord not in visited:
                        new_visited = deepcopy(visited)
                        new_visited.add(new_coord)
                        recur(new_visited, new_coord, path + [new_coord])

        recur({start}, start, [start])

        return len(possible_solutions)
