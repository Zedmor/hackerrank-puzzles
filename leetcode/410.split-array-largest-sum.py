#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (42.98%)
# Total Accepted:    74.6K
# Total Submissions: 171.1K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
#
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#
#
from copy import copy
from functools import lru_cache

def get_array_width(pointers_arr, source_arr, idx):
    if idx == 0:
        return pointers_arr[0] - 0
    if idx >= len(pointers_arr):
        return len(source_arr) - pointers_arr[-1]
    else:
        return pointers_arr[idx] - pointers_arr[idx - 1]



class Solution:
    """
    >>> Solution().splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8)
    2147483647

    >>> Solution().splitArray([1,2147483646], 1)
    2147483647

    >>> Solution().splitArray([7,2,5,10,8], 2)
    18
    """
    def splitArray(self, nums: list, m: int) -> int:

        @lru_cache
        def calc_sum(pointers):
            pointers = list(pointers)
            if not pointers:
                return sum(nums)
            arrays = [nums[0: pointers[0]]]
            for left, right in zip(pointers, pointers[1:] + [len(nums)]):
                arrays.append(nums[left:right])
            return list(map(sum, arrays))

        starting_pointers = tuple(range(1, m))

        @lru_cache
        def dp(pointers):
            for i in range(10):
                sums = calc_sum(pointers)

                max_value = max(sums)
                max_index = sums.index(max_value)

                widths = [get_array_width(pointers, nums, arr_i) for arr_i in range(m)]

                if widths[max_index] > 1:

                    variants = [pointers]

                    try:
                        variant1 = list(pointers[:])
                        variant1[max_index - 1] = variant1[max_index - 1] + 1
                        variants.append(variant1)

                    except IndexError:
                        pass

                    try:
                        variant2 = list(pointers[:])
                        variant2[max_index + 1] = variant2[max_index + 1] - 1
                        variants.append(variant2)
                    except IndexError:
                        pass

                    new_sums = list(map(lambda v: max(calc_sum(tuple(v))), variants))
                    best_variant = new_sums.index(min(new_sums))

                    pointers = tuple(variants[best_variant])

                    print(variants[best_variant])



        dp(starting_pointers)

