#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (38.07%)
# Total Accepted:    298.8K
# Total Submissions: 784.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#
#
from typing import List


class Solution:
    """
    >>> Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    4

    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        if h == 0 or not matrix[0]:
            return 0
        w = len(matrix[0])

        dp = [[0] * (w + 1) for _ in range(h + 1)]

        answer = 0
        for row in range(1, h + 1):
            for col in range(1, w + 1):
                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = 1
                    if row > 0 and col > 0:
                        dp[row][col] += min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])
                    answer = max(answer, dp[row][col])
        return answer * answer




