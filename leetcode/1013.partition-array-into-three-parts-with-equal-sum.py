#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (56.56%)
# Total Accepted:    21.4K
# Total Submissions: 37.7K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array A of integers, return true if and only if we can partition the
# array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with
# (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1]
# + ... + A[A.length - 1])
#
#
#
# Example 1:
#
#
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
#
# Example 2:
#
#
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
#
#
#
# Example 3:
#
#
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
#
#
#
# Note:
#
#
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
#
#
"""
# >>> Solution().canThreePartsEqualSum([30,-23,3,14,-10,4,-6,6,18])
# False

>>> Solution().canThreePartsEqualSum([1,1,1])
True

>>> Solution().canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
True

>>> Solution().canThreePartsEqualSum([259,-226,62,-2,38,45,-121,135,-10,34,-158,127,32,-143,197,-180,107,19,-139,-70,59,25,-1,65,13,-136,157,-142,67,15,61,53,28])
False


>>> Solution().canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
False
"""

cache = {}

def cached(f):
    def wrapped(*args):
        if args in cache:
            return cache[args]
        else:
            r = f(*args)
            cache[args] = r
            return r
    return wrapped


class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        if len(A) < 3:
            return False
        i1 = 0
        i2 = len(A) - 1
        s1 = 0
        s2 = 0
        sm = sum(A)


        while i1 < i2 and i1 < len(A) - 1:

            if A[i1] >= A[i2]:
                i1 += 1
                s1 += A[i1]
                sm -= A[i1]
                if s1 == s2 == sm and i1 > 0 and i2 > i1 + 1:
                    return True
                sm_temp = sm
                s2 = 0
            else:
                i2 -= 1

                s2 += A[i2]
                sm -= A[i2]

                if s1 == s2 == sm and i2 <= len(A) - 1:
                    return True
            sm = sm_temp

        return False




