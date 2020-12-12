#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (62.77%)
# Total Accepted:    173.1K
# Total Submissions: 269.1K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
#
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2.
#
#
#
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
#
#
# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#    For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
#    For number 1 in the first array, the next greater number for it in the
# second array is 3.
#    For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
#
#
#
# Example 2:
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#    For number 2 in the first array, the next greater number for it in the
# second array is 3.
#    For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
#
#
#
#
# Note:
#
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
#
#
#
from bisect import bisect_left
from typing import List


class Solution:
    """
    >>> Solution().nextGreaterElement([4,1,2], [1,3,4,2])
    [-1, 3, -1]


    >>> Solution().nextGreaterElement([2, 4], [1,2,3,4])
    [3, -1]
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp = {}
        ordered_numbers = []
        for el in nums2:
            insertion_point = bisect_left(ordered_numbers, el)
            for lower_els in ordered_numbers[:insertion_point]:
                dp[lower_els] = el
            ordered_numbers = [el] + ordered_numbers[insertion_point:]
        return [dp.get(n, -1) for n in nums1]

