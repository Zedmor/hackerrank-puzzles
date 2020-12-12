#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (43.88%)
# Total Accepted:    24.5K
# Total Submissions: 55.8K
# Testcase Example:  '[1,2,0,0]\n34'
#
# For a non-negative integer X, the array-form of X is an array of its digits
# in left to right order.  For example, if X = 1231, then the array form is
# [1,2,3,1].
#
# Given the array-form A of a non-negative integer X, return the array-form of
# the integer X+K.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
#
#
# Example 2:
#
#
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
#
#
#
# Example 3:
#
#
# Input: A = [2,1,5], K = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
#
#
# Example 4:
#
#
# Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000
#
#
#
#
# Note：
#
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# If A.length > 1, then A[0] != 0
#
#
#
#
#
#
import itertools


def turn_int_to_ary(n):
    arr = []
    while n:
        arr.insert(0, n % 10)
        n = n // 10
    return arr


class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        res = []
        carryover = 0
        for pair in itertools.zip_longest(reversed(A), reversed(turn_int_to_ary(K)), fillvalue=0):
            s = sum(pair) + carryover
            carryover = 0
            if s >= 10:
                s = s - 10
                carryover = 1
            res.insert(0, s)

        if carryover:
            res.insert(0, 1)
        return res

