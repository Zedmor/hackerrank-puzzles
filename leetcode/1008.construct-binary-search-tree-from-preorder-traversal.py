#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (78.63%)
# Total Accepted:    143.7K
# Total Submissions: 182.8K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
#
# It's guaranteed that for the given test cases there is always possible to
# find a binary search tree with the given requirements.
#
# Example 1:
#
#
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.
#
#
#
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    >>> Solution().bstFromPreorder([8,5,1,7,10,12])

    """
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(_id, limit):
            if _id[0] == len(preorder) or preorder[_id[0]] > limit:
                return
            root_value = preorder[_id[0]]
            tree = TreeNode(root_value)
            _id[0] += 1
            tree.left = helper(_id, root_value)
            tree.right = helper(_id, limit)
            return tree
        tree = helper([0], float('inf'))
        return tree


