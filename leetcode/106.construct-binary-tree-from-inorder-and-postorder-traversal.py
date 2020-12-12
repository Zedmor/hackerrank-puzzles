#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (41.24%)
# Total Accepted:    201.9K
# Total Submissions: 459.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
#
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

# from leetcode.treetools import TreeNode, tree2list, list2tree

class Solution:
    """
    >>> tree2list(Solution().buildTree([9,3,15,20,7], [9,15,7,20,3]))
    [3,9,20,null,null,15,7]
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(postorder.pop())
            root.right = self.buildTree(inorder[inorder.index(root.val) + 1:], postorder)
            root.left = self.buildTree(inorder[:inorder.index(root.val)], postorder)
            return root
