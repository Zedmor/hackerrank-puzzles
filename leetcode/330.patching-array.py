#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
# https://leetcode.com/problems/patching-array/description/
#
# algorithms
# Hard (34.16%)
# Total Accepted:    37.3K
# Total Submissions: 107.6K
# Testcase Example:  '[1,3]\n6'
#
# Given a sorted positive integer array nums and an integer n, add/patch
# elements to the array such that any number in range [1, n] inclusive can be
# formed by the sum of some elements in the array. Return the minimum number of
# patches required.
#
# Example 1:
#
#
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
#
# Example 2:
#
#
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
#
#
# Example 3:
#
#
# Input: nums = [1,2,2], n = 5
# Output: 0
#
#
from collections import defaultdict
from copy import deepcopy, copy
from typing import List


class Solution:
    """
    >>> Solution().minPatches([1, 3], 6)
    1

    >>> Solution().minPatches([1,5,10], 20)
    2
    #
    >>> Solution().minPatches([1,2,2], 5)
    0

    """

    def minPatches(self, nums: List[int], n: int) -> int:
        patch, miss, i = 0, 1, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:  # loop till miss = max of the covered range + 1 = (K+1)
                # if nums[i] > miss then nums[i] is out of range even after patching miss e.g. 23 in [1,2,4,23,43]
                miss += nums[
                    i]  # get to the max of the covered range + 1, where +1 comes from initializing miss to be 1
                i += 1
            else:
                miss += miss  # patch miss and lift miss from (K+1) to (2K+2) for finding the new (K+1) for the remaining numbers in nums
                patch += 1  # no. of patches + 1
        return patch





