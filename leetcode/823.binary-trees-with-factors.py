#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#
# https://leetcode.com/problems/binary-trees-with-factors/description/
#
# algorithms
# Medium (35.11%)
# Total Accepted:    12.1K
# Total Submissions: 33.6K
# Testcase Example:  '[2,4]'
#
# Given an array of unique integers, each integer is strictly greater than 1.
#
# We make a binary tree using these integers and each number may be used for
# any number of times.
#
# Each non-leaf node's value should be equal to the product of the values of
# it's children.
#
# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.
#
# Example 1:
#
#
# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
#
# Example 2:
#
#
# Input: A = [2, 4, 5, 10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2,
# 5], [10, 5, 2].
#
#
#
# Note:
#
#
# 1 <= A.length <= 1000.
# 2 <= A[i] <= 10 ^ 9.
#
#
#

from collections import defaultdict
from typing import List


class Solution:
    """
    >>> Solution().numFactoredBinaryTrees([18,3,6,2])
    12

    >>> Solution().numFactoredBinaryTrees([2, 4])
    3

    >>> Solution().numFactoredBinaryTrees([2, 4, 5, 10])
    7

    """
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        dp = defaultdict(dict)
        for i in A:
            for j in A:
                dp[i][j] = i * j

        # trim dp
        for k in list(dp.keys()):
            dp[k] = {k: v for k, v in dp[k].items() if v in dp.keys()}

        counter = defaultdict(int)
        for d in dp.values():
            for v in d.values():
                counter[v] += 1

        res = sum(counter.values())
        return len(A) + res




