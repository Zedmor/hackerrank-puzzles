#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (50.38%)
# Total Accepted:    321.1K
# Total Submissions: 602.6K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 19
#
#
#
from math import factorial


class Solution:
    """
    >>> Solution().numTrees(3)
    5

    """

    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // (factorial(n) * factorial(n + 1))
