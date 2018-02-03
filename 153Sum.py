"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right_pointer = len(nums) - 1
            left_pointer = i + 1
            while left_pointer < right_pointer:
                s = nums[i] + nums[left_pointer] + nums[right_pointer]
                if s > 0:
                    right_pointer -= 1
                elif s < 0:
                    left_pointer += 1
                else:
                    res.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                        right_pointer -= 1
                    left_pointer += 1
                    right_pointer -= 1

        return res


array = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(array))
