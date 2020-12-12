#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (46.82%)
# Total Accepted:    338.5K
# Total Submissions: 715.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from leetcode.treetools import TreeNode, tree2list, list2tree


class Solution:
    """
    >>> tree2list(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
    [3,9,20,null,null,15,7]
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(preorder.pop(0))
            root.left = self.buildTree(preorder, inorder[:inorder.index(root.val)])
            root.right = self.buildTree(preorder, inorder[inorder.index(root.val) + 1:])
            return root




