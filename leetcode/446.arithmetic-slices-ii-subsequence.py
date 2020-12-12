#
# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
#
# algorithms
# Hard (31.05%)
# Total Accepted:    16.6K
# Total Submissions: 53.3K
# Testcase Example:  '[2,4,6,8,10]'
#
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
#
# For example, these are arithmetic sequences:
#
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
# The following sequence is not arithmetic.
#
#
# 1, 1, 2, 5, 7
#
#
# A zero-indexed array A consisting of N numbers is given. A subsequence slice
# of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0
# < P1 < ... < Pk < N.
#
# A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the
# sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this
# means that k ≥ 2.
#
# The function should return the number of arithmetic subsequence slices in the
# array A.
#
# The input contains N integers. Every integer is in the range of -2^31 and
# 2^31-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 2^31-1.
#
#
# Example:
#
#
# Input: [2, 4, 6, 8, 10]
#
# Output: 7
#
# Explanation:
# All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#
#
#
"""
>>> Solution().numberOfArithmeticSlices([1,2,3,4,10,15,20])
4
"""
from math import factorial


class Solution:
    def numberOfArithmeticSlices(self, A: list) -> int:
        diff_array = []

        all_combos = 0

        for i in range(len(A) - 1):
            diff_array.append(A[i + 1] - A[i])
            print(diff_array)
        cur1 = cur2 = 0
        while cur1 < len(diff_array):
            while diff_array[cur2] == diff_array[cur1]:
                cur2 += 1
            len_of_sequence = cur2 - cur1
            if len_of_sequence >= 2:
                all_combos += sum(range(1, len_of_sequence))
            cur1 = cur2




