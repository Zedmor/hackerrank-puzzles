"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search_helper(nums, target, left, right):
            center = (right - left) // 2 + left
            while True:
                if not nums:
                    return -1
                if nums[center] == target:
                    return center
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                if center - left <= 1 and right - center <= 1:
                    return -1
                if nums[center] > nums[left]:
                    if target < nums[left]:
                        left = center
                        center = (right - left) // 2 + left
                        continue
                    if target < nums[center]:
                        right = center
                        center = (right - left) // 2 + left
                        continue
                else:
                    left_res = search_helper(nums, target, left, center)
                    if left_res > 0:
                        return left_res
                    else:
                        left = center
                        center = (right - left) // 2 + left
                if nums[center] < nums[right]:
                    if target > nums[right]:
                        right = center
                        center = (right - left) // 2 + left
                        continue
                    if target > nums[center]:
                        left = center
                        center = (right - left) // 2 + left
                        continue
                else:
                    right_res = search_helper(nums, target, center, right)
                    if right_res > 0:
                        return right_res
                    else:
                        right = center
                        center = (right - left) // 2 + left

        return search_helper(nums, target, 0, len(nums) - 1)





