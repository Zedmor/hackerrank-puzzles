#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.03%)
# Total Accepted:    351.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
from itertools import tee
from typing import List


class Solution:
    """
    >>> Solution().nextPermutation([2, 3, 0, 2, 4, 1])
    [2, 3, 0, 4, 1, 2]

    >>> Solution().nextPermutation([1, 5, 1])
    [5, 1, 1]

    >>> Solution().nextPermutation([2, 3, 1])
    [3, 1, 2]

    >>> Solution().nextPermutation([1, 2, 3])
    [1, 3, 2]

    >>> Solution().nextPermutation([3, 2, 1])
    [1, 2, 3]

    >>> Solution().nextPermutation([1, 1, 5])
    [1, 5, 1]

    >>> Solution().nextPermutation([1, 2, 5, 4, 3])
    [1, 3, 2, 4, 5]
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def pairwise(iterable):
            "s -> (s0,s1), (s1,s2), (s2, s3), ..."
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)

        if len(nums) < 2:
            return

        for i, (a, b) in enumerate(pairwise(nums[::-1])):
            if a > b:
                break
        else:
            nums.sort()
            return

        i += 1
        i = len(nums) - 1 - i

        max_diff = float('inf')
        for j in range(i + 1, len(nums)):
            if nums[j] != nums[i] and abs(nums[j] - nums[i]) < max_diff and nums[j] > nums[i]:
                target = j
                max_diff = abs(nums[j] - nums[i])

        nums[i], nums[target] = nums[target], nums[i]

        nums[i + 1:] = sorted(nums[i + 1:])
