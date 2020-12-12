#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (43.76%)
# Total Accepted:    75.6K
# Total Submissions: 169K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
#
#
#
# Example 1:
#
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
#
#
# Note:
#
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#
#
#
from copy import copy
from typing import List


def even_sum(pointers, nums):
    """
    # >>> even_sum([1, 2], [5, 5, 5])
    # True
    #
    # >>> even_sum([1, 2], [5, 5, 2, 3])
    # True
    #
    # >>> even_sum([1, 3], [5, 2, 3, 5])
    # True
    #
    # >>> even_sum([1, 3], [5, 2, 3, 6])
    # False

    :param pointers:
    :return:
    """
    running_sum = sum(nums[0:pointers[0]])
    start = 0
    temp_pointers = copy(pointers)
    temp_pointers.append(len(nums))
    for pointer in temp_pointers:
        if sum(nums[start: pointer]) != running_sum:
            return False
        start = pointer
    return True

class Solution:
    """
    >>> Solution().canPartitionKSubsets([2,2,2,2,3,4,5], 4)
    False

    >>> Solution().canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3)
    True

    >>> Solution().canPartitionKSubsets([1,2,3,4], 3)
    False

    >>> Solution().canPartitionKSubsets([2,3,4,5,6,7,8,9], 3)
    False

    >>> Solution().canPartitionKSubsets([4,3,2,3,5,2,1], 2)
    True

    """
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def isSubsetSum(arr, n, numsum, excluded_ns, level):
            # Base Cases
            if numsum == 0:
                if excluded_ns == [] and level == 1:
                    return True
                else:
                    return isSubsetSum(excluded_ns, len(excluded_ns), sum(nums) / k, [], level - 1)
            if n == 0 and numsum != 0:
                return False

            # If last element is greater than sum, then
            # ignore it
            # if arr[n - 1] > sum:
            #     return isSubsetSum(arr, n - 1, sum, excluded_ns)

            ''' else, check if sum can be obtained by any of  
            the following 
            (a) including the last element 
            (b) excluding the last element'''

            return isSubsetSum(
                arr,
                n - 1,
                numsum,
                copy(excluded_ns) + [arr[n-1]], level) or isSubsetSum(
                arr,
                n - 1,
                numsum - arr[n - 1],
                excluded_ns, level)

        if sum(nums) % k != 0:
            return False
        each_array_sum = sum(nums) / k
        return isSubsetSum(nums, len(nums), each_array_sum, [], k)



