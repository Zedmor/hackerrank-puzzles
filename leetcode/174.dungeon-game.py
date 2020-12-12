#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
# https://leetcode.com/problems/dungeon-game/description/
#
# algorithms
# Hard (29.38%)
# Total Accepted:    112.7K
# Total Submissions: 346.4K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# table.dungeon, .dungeon th, .dungeon td {
#  border:3px solid black;
# }
#
# .dungeon th, .dungeon td {
#    text-align: center;
#    height: 70px;
#    width: 70px;
# }
#
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the
# princess.
#
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or
# contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to
# move only rightward or downward in each step.
#
#
#
# Write a function to determine the knight's minimum initial health so that he
# is able to rescue the princess.
#
# For example, given the dungeon below, the initial health of the knight must
# be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN ->
# DOWN.
#
#
#
#
# -2 (K)
# -3
# 3
#
#
# -5
# -10
# 1
#
#
# 10
# 30
# -5 (P)
#
#
#
#
#
#
# Note:
#
#
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight
# enters and the bottom-right room where the princess is imprisoned.
#
#
#
from collections import namedtuple
from typing import List


class Solution:
    """
    >>> Solution().calculateMinimumHP([[3],[49],[38],[30],[-93],[-99],[13],[10],[6],[-77],[-83],[-76],[24],[-40],[-73]])
    369

    >>> Solution().calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]])
    3

    >>> Solution().calculateMinimumHP([[0,0,0],[1,1,-1]])
    1

    >>> Solution().calculateMinimumHP([[0, 0]])
    1

    >>> Solution().calculateMinimumHP([[2],[1]])
    1

    >>> Solution().calculateMinimumHP([[0,-5],[0,0]])
    1

    >>> Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    7

    """

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        Cell = namedtuple('Cell', ['y', 'x'])

        m = len(dungeon[0])  # width
        n = len(dungeon)  # height
        dp = {Cell(y=n - 1, x=m - 1): max(1, 1 - dungeon[n - 1][m - 1])}

        cursor_x = max(m - 2, 0)
        cursor_y = max(n - 2, 0)

        while cursor_x >= 0 or cursor_y >= 0:
            x = m - 1
            y = n - 1
            while x >= cursor_x or y >= cursor_y:

                if y >= 0:
                    y_cell = Cell(y, cursor_x)
                    candidates = [dp.get(y_cell, float('inf'))]
                    if m - 1 > cursor_x > -2:
                        candidates.append(max(dp[Cell(y, cursor_x + 1)] - dungeon[y][cursor_x], 1))

                    if n - 1 > y >= 0 and cursor_x >= 0:
                        candidates.append(max(dp[Cell(y + 1, cursor_x)] - dungeon[y][cursor_x], 1))
                    dp[y_cell] = min(candidates)

                if x >= 0:
                    x_cell = Cell(cursor_y, x)
                    candidates = [dp.get(x_cell, float('inf'))]
                    if n - 1 > cursor_y > -2:
                        candidates.append(max(dp[Cell(cursor_y + 1, x)] - dungeon[cursor_y][x], 1))
                    if m - 1 > x >= 0 and cursor_y >= 0:
                        candidates.append(max(dp[Cell(cursor_y, x + 1)] - dungeon[cursor_y][x], 1))
                    dp[x_cell] = min(candidates)

                if x >= cursor_x:
                    x -= 1
                if y >= cursor_y:
                    y -= 1

            cursor_x -= 1
            cursor_y -= 1

        return dp[Cell(0, 0)]
