#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (62.94%)
# Total Accepted:    55.6K
# Total Submissions: 88.8K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
#
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#
def merge(sorted_left, sorted_right):
    i = 0
    j = 0
    result = []
    while i < len(sorted_left) or j < len(sorted_right):
        if j == len(sorted_right):
            result.append(sorted_left[i])
            i += 1
            continue
        if i == len(sorted_left):
            result.append(sorted_right[j])
            j += 1
            continue
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
            result.append(sorted_right[j])
            j += 1
    return result



class Solution:
    """
    # >>> Solution().sortArray([5, 2, 3, 1])
    # [1, 2, 3, 5]

    >>> Solution().sortArray([5,1,1,2,0,0])
    [0, 0, 1, 1, 2, 5]
    """
    def sortArray(self, nums: list) -> list:
        if len(nums) == 2:
            if nums[1] < nums[0]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums
        elif len(nums) > 2:
            right_part = nums[:len(nums) // 2]
            left_part = nums[len(nums) // 2:]
            sorted_left = self.sortArray(left_part)
            sorted_right = self.sortArray(right_part)
            nums = merge(sorted_left, sorted_right)
            return nums
        else:
            return nums


