#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (67.32%)
# Total Accepted:    305.5K
# Total Submissions: 438K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,1]
#
# Example 2:
#
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
#
#
from math import sqrt
from typing import List


class Solution:
    """
    >>> Solution().countBits(2)
    [0, 1, 1]

    >>> Solution().countBits(5)
    [0, 1, 1, 2, 1, 2]

    """
    def countBits(self, num: int) -> List[int]:
        dp = [0, 1]
        while len(dp) <= num:
            for i in range(len(dp)):
                dp.append(1 + dp[i])
        return dp[:num + 1]
