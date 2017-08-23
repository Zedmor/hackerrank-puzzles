"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
import random


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(1,len(nums)):
            r = random.randint(i, len(nums)-1)
            nums[i], nums[r] = nums[r], nums[i]
            print(nums)



z = Solution().permuteUnique([1, 1, 2])
