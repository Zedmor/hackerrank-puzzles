#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (35.52%)
# Total Accepted:    98.5K
# Total Submissions: 270.6K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges
# between them.
#
#
#
# Example 1:
#
# Input:
#
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
#
#
# Output:  2
#
#
#
# Example 2:
#
# Input:
#
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
#
#
# Output:  2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
#
#
# Definition for a binary tree node.
from leetcode.treetools import list2tree
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    >>> Solution().longestUnivaluePath(list2tree(data))
    318

    >>> Solution().longestUnivaluePath(list2tree('[1,1,1]'))
    2

    >>> Solution().longestUnivaluePath(list2tree('[1,null,1,1,1,1,1,1]'))
    4

    >>> Solution().longestUnivaluePath(list2tree('[1,1]'))
    1

    >>> Solution().longestUnivaluePath(list2tree('[1]'))
    0

    >>> Solution().longestUnivaluePath(list2tree('[5,4,5,1,1,null,5]'))
    2

    >>> Solution().longestUnivaluePath(list2tree('[1,4,5,4,4,5]'))
    2

    """

    def __init__(self):
        self.best_result = 0

    def update_best_result(self, v):
        if v > self.best_result:
            self.best_result = v

    def longestUnivaluePath(self, root: TreeNode) -> int:
        import sys

        sys.setrecursionlimit(10 ** 6)
        self.update_best_result(self.recur(root))
        return self.best_result

    @lru_cache(2048)
    def recur(self, node, depth=0):

        if not node:
            return 0

        left_result = self.recur(node.left)
        self.update_best_result(left_result)

        right_result = self.recur(node.right)
        self.update_best_result(right_result)

        if node.left and node.right and node.val == node.left.val and node.val == node.right.val:
            self.update_best_result(left_result + right_result)

        result_cont = [0]
        if node.left and node.left.val == node.val:
            result_cont.append(self.recur(node.left, depth + 1))
        if node.right and node.right.val == node.val:
            result_cont.append(self.recur(node.right, depth + 1))

        if depth == 0:
            self.update_best_result(sum(result_cont))

        return max(result_cont + [depth])


data = '[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null]'


