#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (60.20%)
# Total Accepted:    174.8K
# Total Submissions: 269.5K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
#
# Follow up: Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant space complexity?
#
#
# Example 1:
#
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
#
# Example 2:
#
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
#
# Example 3:
#
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 30000
# Each integer in nums will appear twice, only two integers will appear once.
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().singleNumber([1,2,1,3,2,5])
    [3, 5]

    >>> Solution().singleNumber([-1,0])
    [-1, 0]

    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        cache = set()
        for n in nums:
            if n in cache:
                cache.remove(n)
            else:
                cache.add(n)

        return list(cache)


