#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (45.47%)
# Total Accepted:    505.8K
# Total Submissions: 1.1M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand. (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Return the minimum element of this array.
#
#
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Example 3:
# Input: nums = [1]
# Output: 1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated at some pivot.
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().findMin([2,3,4,5,6,1])
    1

    >>> Solution().findMin([5,1,2,3,4])
    1

    >>> Solution().findMin([2, 3, 1])
    1

    >>> Solution().findMin([1, 2, 3])
    1

    >>> Solution().findMin([2, 1])
    1

    >>> Solution().findMin([3,4,5,1,2])
    1

    >>> Solution().findMin([4,5,6,7,0,1,2])
    0

    >>> Solution().findMin([1])
    1

    """

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[0] < nums[-1]:
            return nums[0]

        while left <= right:
            mid = (right + left) // 2

            if mid < right and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if mid > left and nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1

            else:
                right = mid - 1

        return nums[mid]
