#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (44.47%)
# Total Accepted:    33.9K
# Total Submissions: 75.1K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
#
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
#
# Example:
#
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
#
#
#
#
# Note:
#
#
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
#
#
#
#
#
import functools


def add_elements(param, param1):
    return param[0] + param1[0], param[1] + param1[1]

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k: int) -> list:
        items = {}
        for i in range(len(nums) - k + 1):
            items[i] = sum(nums[i:i+k])

        @functools.lru_cache()
        def knapsack(n, c):
            if n > len(nums) - k or c == 0:
                result = (0, [])
            else:
                tmp1 = knapsack(n + 1, c)
                tmp2 = add_elements((items[n], [n]), knapsack(n + k, c - 1))
                result = max(tmp1, tmp2) if tmp1[0] != tmp2[0] else min(tmp1, tmp2, key=lambda t: t[1])
            return result

        return knapsack(0, 3)[1]


