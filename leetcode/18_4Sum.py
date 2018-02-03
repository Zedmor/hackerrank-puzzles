"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from collections import defaultdict


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        targets = defaultdict(list)
        for i, n in enumerate(nums):
            targets[target - n].append(i)
        sorted_keys = sorted(targets)
        res = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right_pointer = len(nums) - 1
            left_pointer = i + 1
            while left_pointer < right_pointer:
                for cursor in range(left_pointer+1, right_pointer):
                    s = nums[i] + nums[left_pointer] + nums[right_pointer] + nums[cursor]

                    if s > target:
                        right_pointer -= 1
                    elif s < target:
                        left_pointer += 1
                    else:
                        res.append([nums[i], nums[left_pointer], nums[right_pointer], nums[cursor]])
                        while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                            left_pointer += 1
                        while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                            right_pointer -= 1
                        left_pointer += 1
                        right_pointer -= 1

        return res

array = [1, 0, -1, 0, -2, 2]

print(Solution().fourSum(array, 0))
