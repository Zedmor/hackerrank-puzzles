#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (50.61%)
# Total Accepted:    103.2K
# Total Submissions: 197.8K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
from functools import lru_cache
from typing import List


class Solution:
    """
    # >>> Solution().maxCoins([8,3,4,3,5,0,5,6,6])
    # 1100

    >>> Solution().maxCoins([3, 1, 5, 8])
    167

    """
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        @lru_cache(maxsize=2000000)
        def recur(i, j):
            if i + 1 >= j:
                return 0
            results = []
            for k in range(i + 1, j):
                coins = nums[k] * nums[i] * nums[j]
                results.append(recur(i, k) + recur(k, j) + coins)

            return max(results) if results else 0

        nums.append(1)
        result = recur(-1, len(nums) - 1)
        # print(recur.cache_info())
        return result


