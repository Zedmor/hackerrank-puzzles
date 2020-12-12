#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.34%)
# Total Accepted:    650.2K
# Total Submissions: 2.4M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Definition for a binary tree node.
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution:
    """
    >>> Solution().isValidBST(deserialize('[10,5,15,null,null,6,20]'))
    False

    >>> Solution().isValidBST(deserialize('[5,1,4,null,null,3,6]'))
    False

    >>> Solution().isValidBST(deserialize('[2,1,3]'))
    True

    """

    def isValidBST(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return True
            left_nodes = []
            right_nodes = []
            if node.left:
                left_nodes = check(node.left)
                if any(node.val <= x for x in left_nodes):
                    raise ValueError('Incorrect node found')
            if node.right:
                right_nodes = check(node.right)
                if any(node.val >= x for x in right_nodes):
                    raise ValueError('Incorrect node found')
            return [node.val] + left_nodes + right_nodes

        try:
            check(root)
            return True
        except ValueError:
            return False
