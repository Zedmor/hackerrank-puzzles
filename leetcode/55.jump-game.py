#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.65%)
# Total Accepted:    311.5K
# Total Submissions: 954.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
"""

>>> Solution().canJump([3,0,8,2,0,0,1])
True

>>> Solution().canJump([2, 0, 0])
True

>>> Solution().canJump([0])
True

>>> Solution().canJump([1])
True

>>> Solution().canJump([2,3,1,1,4])
True

>>> Solution().canJump([2, 0])
True

>>> Solution().canJump([3,2,1,0,4])
False
"""
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def canJump(self, nums: list) -> bool:
        if nums == [1]:
            return True

        graph = defaultdict(set)
        intervals = []
        for i, element in enumerate(nums):
            interval = (i, i + element)
            graph[interval].add(i)
            intervals.append(interval)

        sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
        merged = []

        for higher in sorted_by_lower_bound:
            if not merged:
                merged.append(higher)
            else:
                lower = merged[-1]
                # test for intersection between lower and higher:
                # we know via sorting that lower[0] <= higher[0]
                if higher[0] <= lower[1]:
                    upper_bound = max(lower[1], higher[1])
                    merged[-1] = (lower[0], upper_bound)  # replace by merged interval
                else:
                    merged.append(higher)
        return len(merged) == 1 and merged[0][0] == 0 and merged[0][1] >= len(nums) - 1








