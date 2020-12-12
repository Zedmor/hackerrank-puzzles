#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (44.85%)
# Total Accepted:    85.9K
# Total Submissions: 190.4K
# Testcase Example:  '[1,3,5,4,7]'
#
#
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
#
#
# Example 1:
"""
>>> Solution().findLengthOfLCIS([1,3,5,4,7])
3

# Explanation: The longest continuous increasing subsequence is [1,3,5], its
# length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4.
#
#
#
# Example 2:

>>> Solution().findLengthOfLCIS([2,2,2,2,2])
1


>>> Solution().findLengthOfLCIS([1, 3, 5, 7])
4
"""

# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length
# is 1.
#
#
#
# Note:
# Length of the array will not exceed 10,000.
#
#
class Solution:
    def findLengthOfLCIS(self, nums) -> int:

        longest = 0

        if len(nums) < 2:
            return len(nums)
        i = 0
        j = 0
        while j < len(nums):

            if nums[j] <= nums[j - 1]:
                i = j
            j += 1
            if j - i > longest:
                longest = j - i
        return longest


