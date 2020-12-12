#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (36.10%)
# Total Accepted:    159.5K
# Total Submissions: 441.8K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
import itertools
from copy import copy
from functools import lru_cache
from typing import List


def cal_rob_sum(l, rob_pattern):
    return sum(itertools.compress(l, rob_pattern))


class Solution:
    """
    >>> Solution().rob([2,7,9,3,1])
    11

    >>> Solution().rob([2, 1, 1, 2])
    3

    # >>> Solution().rob([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, ])
    # 1
    #
    >>> Solution().rob([1])
    1

    >>> Solution().rob([])
    0

    >>> Solution().rob([1, 2, 3, 1])
    4

    >>> Solution().rob([2, 3, 2])
    3


    """
    def rob_(self, nums: List[int]) -> int:

        frozen_nums = tuple(nums)

        def calculate_max(rob_pattern, rob_cursor):
            if not rob_pattern:
                return 0
            if rob_cursor == len(rob_pattern):
                return cal_rob_sum(frozen_nums, rob_pattern)
            new_pattern = copy(rob_pattern)
            right_house_safe = new_pattern[rob_cursor+1] == 0 if rob_cursor < len(nums) - 1 else new_pattern[0] == 0
            if right_house_safe and new_pattern[rob_cursor - 1] == 0 and rob_pattern[rob_cursor] == 0:
                new_pattern[rob_cursor] = 1
                return max(calculate_max(new_pattern, rob_cursor + 1), calculate_max(rob_pattern, rob_cursor +
                                                                                            1))

            else:
                return calculate_max(rob_pattern, rob_cursor + 1)

        rob_pattern = [0] * len(nums)
        return calculate_max(rob_pattern, 0)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = {}
        dp2 = {}
        dp[(0, True)] = nums[0]
        dp[(0, False)] = 0
        dp2[(0, True)] = 0
        dp2[(0, False)] = 0
        for i in range(1, len(nums)):
            dp[(i, True)] = max(dp.get((i-1, False), 0) + nums[i], dp.get((i-2, True), 0) + nums[i], dp.get((i-2, False), 0) + nums[i])
            dp2[(i, True)] = max(dp2.get((i - 1, False), 0) + nums[i], dp2.get((i - 2, True), 0) + nums[i],
                                    dp2.get((i - 2, False), 0) + nums[i])
            dp[(i, False)] = max(dp.get((i-1, True), 0), dp.get((i-1, False), 0))
            dp2[(i, False)] = max(dp2.get((i - 1, True), 0), dp2.get((i - 1, False), 0))

        return max(dp[(i, False)], dp2[(i, True)])
