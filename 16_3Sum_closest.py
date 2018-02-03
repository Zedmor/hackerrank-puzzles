"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = float('inf')
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            right_pointer = len(nums) - 1
            left_pointer = i + 1
            closest = None
            current_distance = float('inf')
            while left_pointer < right_pointer:
                s = nums[i] + nums[left_pointer] + nums[right_pointer]
                if s > target:
                    right_pointer -= 1
                elif s < target:
                    left_pointer += 1
            if abs(target - res) > abs(target - s):
                res = s

        return res


array = [0,1,2]

print(Solution().threeSumClosest(array, 1))
