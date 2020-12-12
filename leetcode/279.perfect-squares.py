#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (45.21%)
# Total Accepted:    316K
# Total Submissions: 668.8K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
import math


class Solution:
    """
    >>> Solution().numSquares(12)
    3

    >>> Solution().numSquares(13)
    2

    >>> Solution().numSquares(6052)
    2

    """
    def numSquares(self, n: int) -> int:
        dp = [(0, i) for i in range(n + 1)]
        ans = 0

        squares = []
        for i in range(1, int(math.sqrt(n)) + 1):
            squares.append(i ** 2)

        for i in range(n+1):
            for j in range(len(squares) - 1, -1, -1):
                if squares[j] <= i:
                    candidate, count = dp[i - squares[j]]
                    candidate += squares[j]
                    if candidate >= dp[i][0] and count + 1 <= dp[i][1]:
                        dp[i] = (candidate, count + 1)

        return dp[n][1]

