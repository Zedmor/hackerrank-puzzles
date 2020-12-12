#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#
# https://leetcode.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (46.14%)
# Total Accepted:    8.6K
# Total Submissions: 18.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
#
#
# Example 2:
#
#
# Input: grid = [[1,1,0,0]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] is 0 or 1
#
#
from typing import List


def search_square(grid, i, j):
    """
    >>> search_square([[1,1,1],[1,0,1],[1,1,1]], 0 , 0)
    3

    >>> search_square([[1,0,1],[1,0,1],[1,1,1]], 0 , 0)
    1

    >>> search_square([[1,1,0],[1,1,0],[0,0,0]], 0 , 0)
    2

    """
    skip_this = False
    size = 0
    best_size = 0
    while size + i < len(grid) and size + j < len(grid[0]):
        if grid[i + size][j] == 0 or grid[i][j + size] == 0:
            return best_size
        for m in range(i, size + i + 1):
            if grid[m][j + size] == 0:
                skip_this = True
        for n in range(j, size + j + 1):
            if grid[i + size][n] == 0:
                skip_this = True


        size += 1
        if not skip_this:
            best_size = size
        skip_this = False
    return best_size

class Solution:
    """
    >>> Solution().largest1BorderedSquare([[0,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,0],[0,1,1,1,1],[1,1,1,0,1],[0,1,1,1,1],[1,1,1,0,1]])
    9

    >>> Solution().largest1BorderedSquare([[1,1,1,0],[1,0,1,1],[1,1,0,0],[1,1,1,1],[0,1,0,1]])
    4

    >>> Solution().largest1BorderedSquare([[1,0],[0,0]])
    1

    >>> Solution().largest1BorderedSquare([[0]])
    0

    >>> Solution().largest1BorderedSquare([[1,1],[1,0]])
    1

    >>> Solution().largest1BorderedSquare([[0,0],[0,1]])
    1

    >>> Solution().largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]])
    9

    >>> Solution().largest1BorderedSquare([[1,1,0,0]])
    1

    """
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0
        if len(grid) == 0:
            return 0
        all_sizes = set()
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                size = search_square(grid, i, j)
                all_sizes.add(size ** 2)
                # j = min(len(grid[0]), max(j + size, j + 1))
                j += 1
            i += 1

        return max(all_sizes)



