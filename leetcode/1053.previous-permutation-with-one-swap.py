#
# @lc app=leetcode id=1053 lang=python3
#
# [1053] Previous Permutation With One Swap
#
# https://leetcode.com/problems/previous-permutation-with-one-swap/description/
#
# algorithms
# Medium (48.20%)
# Total Accepted:    14.4K
# Total Submissions: 29.6K
# Testcase Example:  '[3,2,1]'
#
# Given an array A of positive integers (not necessarily distinct), return the
# lexicographically largest permutation that is smaller than A, that can be
# made with one swap (A swap exchanges the positions of two numbers A[i] and
# A[j]).   If it cannot be done, then return the same array.
#
#
#
# Example 1:
#
#
# Input: [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.
#
#
# Example 2:
#
#
# Input: [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.
#
#
# Example 3:
#
#
# Input: [1,9,4,6,7]
# Output: [1,7,4,6,9]
# Explanation: Swapping 9 and 7.
#
#
# Example 4:
#
#
# Input: [3,1,1,3]
# Output: [1,3,1,3]
# Explanation: Swapping 1 and 3.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 10000
# 1 <= A[i] <= 10000
#
#
#
from copy import copy
from typing import List
import bisect

class Solution:
    """
    >>> Solution().prevPermOpt1([1,9,4,6,7])
    [1, 7, 4, 6, 9]

    >>> Solution().prevPermOpt1([3,1,1,3])
    [1, 3, 1, 3]

    """
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        perms = []
        for i in range(len(A)):
            for j in range(i):
                new_a = copy(A)
                new_a[j], new_a[i] = new_a[i], new_a[j]
                if new_a < A:
                    bisect.insort_left(perms, tuple(new_a))
        if perms:
            return list(perms[-1])
        else:
            return A


