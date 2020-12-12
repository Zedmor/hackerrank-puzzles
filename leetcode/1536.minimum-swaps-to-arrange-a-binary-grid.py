#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
#
# algorithms
# Medium (42.77%)
# Total Accepted:    7.6K
# Total Submissions: 17.8K
# Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
#
# Given an n x n binary grid, in one step you can choose two adjacent rows of
# the grid and swap them.
#
# A grid is said to be valid if all the cells above the main diagonal are
# zeros.
#
# Return the minimum number of steps needed to make the grid valid, or -1 if
# the grid cannot be valid.
#
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and
# ends at cell (n, n).
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
#
#
# Example 3:
#
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] is 0 or 1
#
#
#
from copy import copy
from functools import lru_cache
from typing import List


def is_valid(grid, order):
    for i, row in enumerate(order):
        for col in range(i + 1, len(grid)):
            if grid[row][col] != 0:
                return False
    return True


class Solution:
    """
    >>> Solution().minSwaps(grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]])
    2

    >>> Solution().minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]])
    3

    """
    def minSwaps(self, grid: List[List[int]]) -> int:
        v = set()
        v.add(tuple(range(len(grid))))

        @lru_cache(None)
        def dfs(order, depth=0, visited=None):
            if not visited:
                visited = set()

            if is_valid(grid, order):

                return depth
            results = []
            for i in range(len(order) - 1):
                copy_order = list(order)
                copy_order[i], copy_order[i + 1] = copy_order[i + 1], copy_order[i]
                if tuple(copy_order) not in visited:
                    new_visited = set(visited)
                    new_visited.add(tuple(copy_order))
                    results.append(dfs(tuple(copy_order), depth + 1, frozenset(new_visited)))
            return min(results) if results else float('inf')

        result = dfs(tuple(range(len(grid))), depth=0, visited=frozenset(v))
        return result if result != float('inf') else -1
