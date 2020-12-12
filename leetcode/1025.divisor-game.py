#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#
# https://leetcode.com/problems/divisor-game/description/
#
# algorithms
# Easy (65.54%)
# Total Accepted:    66.2K
# Total Submissions: 100K
# Testcase Example:  '2'
#
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number N on the chalkboard.  On each player's turn,
# that player makes a move consisting of:
#
#
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
#
#
# Also, if a player cannot make a move, they lose the game.
#
# Return True if and only if Alice wins the game, assuming both players play
# optimally.
#
# Example 1:
#
#
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
#
#
#
# Example 2:
#
#
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more
# moves.
#
#
#
#
# Note:
#
#
# 1 <= N <= 1000
#
#
#
#
from collections import defaultdict
from functools import lru_cache


class Solution:
    """
    >>> Solution().divisorGame(454)
    True

    >>> Solution().divisorGame(8)
    True

    >>> Solution().divisorGame(2)
    True

    >>> Solution().divisorGame(3)
    False

    """
    def divisorGame(self, N: int) -> bool:
        dp = defaultdict(list)
        for i in range(1, N + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i].append(i - j)

        solution = {}

        for i in range(1, N + 1):
            if 1 in dp[i]:
                solution[i] = True
            else:
                solution[i] = not all(solution[v] for v in dp[i])

        return solution[N]
