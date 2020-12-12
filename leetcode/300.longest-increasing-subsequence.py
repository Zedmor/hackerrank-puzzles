#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.16%)
# Total Accepted:    419.6K
# Total Submissions: 981.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
# Note:
#
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
#
from bisect import bisect, bisect_left
from typing import List


class Solution:
    """
    # >>> Solution().lengthOfLIS(list(range(1, 2501)))
    # 2500
    #
    # >>> Solution().lengthOfLIS([4,10,4,3,8,9])
    # 3
    #
    # >>> Solution().lengthOfLIS([0])
    # 1

    >>> Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    4

    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = []
        for n in nums:
            insertion_point = bisect_left(lengths, n)
            if insertion_point == len(lengths):
                lengths.append(n)
            else:
                lengths[insertion_point] = n
        return len(lengths)
