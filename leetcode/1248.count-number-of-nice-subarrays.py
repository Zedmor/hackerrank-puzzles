#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#
# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (55.02%)
# Total Accepted:    20.6K
# Total Submissions: 36.4K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# Given an array of integers nums and an integer k. A subarray is called nice
# if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and
# [1,2,1,1].
#
#
# Example 2:
#
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
#
#
# Example 3:
#
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
#
#
#
from functools import lru_cache
from typing import List


class Solution:
    """
    >>> Solution().numberOfSubarrays([2044,96397,50143], 1)
    3

    >>> Solution().numberOfSubarrays([1,1,1,1,1], 1)
    5

    >>> Solution().numberOfSubarrays([1,1,2,1,1], 3)
    2

    >>> Solution().numberOfSubarrays([2,4,6], 1)
    0

    >>> Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)
    16

    """

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        solutions = set()

        i = 0
        j = 0
        n_odds = 0

        while j < len(nums):
            j += 1
            if nums[j - 1] % 2 == 1:
                n_odds += 1
            if n_odds == k:
                solutions.add((i, j))
            if j == len(nums) + 1:
                break
            while n_odds > k:
                if nums[i] % 2 == 1:
                    n_odds -= 1
                i += 1
            if n_odds == k:
                solutions.add((i, j))
            if n_odds == k:
                old_i = i
                old_n_odds = n_odds
                while n_odds == k and i < j - 1:
                    if nums[i] % 2 == 1:
                        n_odds -= 1
                    i += 1
                    if n_odds == k:
                        solutions.add((i, j))

                i = old_i
                n_odds = old_n_odds
        # print(solutions)
        return len(solutions)




