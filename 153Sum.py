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
        nums = sorted(nums) # O(n log n)
        set_nums = set(nums) # O(n)
        found_triplets = set()
        while nums:
            first_element = nums.pop(0)





array = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(array))