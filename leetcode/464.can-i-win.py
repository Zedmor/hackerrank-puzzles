#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (28.56%)
# Total Accepted:    54.6K
# Total Submissions: 186K
# Testcase Example:  '10\n11'
#
# In the "100 game" two players take turns adding, to a running total, any
# integer from 1 to 10. The player who first causes the running total to reach
# or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of
# numbers from 1 to 15 without replacement until they reach a total >= 100.
#
# Given two integers maxChoosableInteger and desiredTotal, return true if the
# first player to move can force a win, otherwise return false. Assume both
# players play optimally.
#
#
# Example 1:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
#
#
# Example 2:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
#
#
# Example 3:
#
#
# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= maxChoosableInteger <= 20
# 0 <= desiredTotal <= 300
#
#
#
from copy import copy
from functools import lru_cache


class Solution:
    """
    >>> Solution().canIWin(5, 50)
    False

    >>> Solution().canIWin(20, 210)
    False

    >>> Solution().canIWin(4, 6)
    True

    >>> Solution().canIWin(10, 40)
    False

    >>> Solution().canIWin(10, 0)
    True

    >>> Solution().canIWin(10, 1)
    True

    >>> Solution().canIWin(10, 11)
    False

    """

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        @lru_cache(None)
        def recur(running_sum, bag):

            for el in bag:
                if not recur(running_sum + el, bag - {el}) or el + running_sum >= desiredTotal:
                    return True
            return False

        start_bag = frozenset(range(1, maxChoosableInteger + 1))
        if sum(start_bag) < desiredTotal:
            return False
        return recur(0, start_bag)
