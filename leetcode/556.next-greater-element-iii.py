#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (31.89%)
# Total Accepted:    47.3K
# Total Submissions: 148.2K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
#
# Example 1:
#
#
# Input: 12
# Output: 21
#
#
#
#
# Example 2:
#
#
# Input: 21
# Output: -1
#
#
#
#
#
import heapq
from copy import copy


class Solution:
    """
    >>> Solution().nextGreaterElement(12443322)
    13222344

    >>> Solution().nextGreaterElement(321)
    -1

    >>> Solution().nextGreaterElement(230241)
    230412

    >>> Solution().nextGreaterElement(12)
    21

    >>> Solution().nextGreaterElement(21)
    -1

    """
    def nextGreaterElement(self, n: int) -> int:
        backup = n
        n = list(str(n))
        stop = False
        for i in range(len(n) - 1, -1, -1):
            for j in range(len(n) - 1, i, -1):
                if n[i] < n[j]:
                    n[i], n[j] = n[j], n[i]
                    stop = True
                    break
            if stop:
                break
        if not stop:
            return -1

        for i in range(i + 1, len(n)):
            for j in range(i, len(n)):
                if n[j] < n[i]:
                    n[i], n[j] = n[j], n[i]

        result = int(''.join(n))
        if result == backup or result > 2_147_483_647:
            return -1
        return result
