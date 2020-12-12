#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (57.16%)
# Total Accepted:    10K
# Total Submissions: 17.5K
# Testcase Example:  '4'
#
# For some fixed N, an array A is beautiful if it is a permutation of the
# integers 1, 2, ..., N, such that:
#
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] +
# A[j].
#
# Given N, return any beautiful array A.  (It is guaranteed that one
# exists.)
#
#
#
# Example 1:
#
#
# Input: 4
# Output: [2,1,4,3]
#
#
#
# Example 2:
#
#
# Input: 5
# Output: [3,1,2,5,4]
#
#
#
#
# Note:
#
#
# 1 <= N <= 1000
#
#
#
#
#
#
from copy import copy
from functools import lru_cache
from typing import List


class Solution:
    """
    >>> Solution().beautifulArray(15)
    [1, 3, 2]

    >>> Solution().beautifulArray(3)
    [1, 3, 2]

    >>> Solution().beautifulArray(4)
    [2, 1, 4, 3]

    >>> Solution().beautifulArray(5)
    [3, 1, 2, 5, 4]

    """
    def beautifulArray(self, N: int) -> List[int]:

        @lru_cache()
        def not_feasable(arr):
            for p in range(1, len(arr) - 1):
                for n in range(p):
                    for l in range(p + 1, len(arr)):
                        if arr[p] * 2 == arr[n] + arr[l]:
                            return True
            return False


        def recursive(el, nums):
            if not_feasable(tuple([e for e in nums if e is not None])):
                return False
            if el == N + 1:
                return nums
            for p, v in enumerate(nums):
                if v is None:
                    attempt = copy(nums)
                    attempt[p] = el
                    result = recursive(el + 1, attempt)
                    if result:
                        return result
            return False

        return recursive(1, [None] * N)



