#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.88%)
# Total Accepted:    396.6K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its minimum depth = 2.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from leetcode.treetools import TreeNode, list2tree


class Solution:
    """
    >>> Solution().minDepth(list2tree('[1,2]'))
    2

    >>> Solution().minDepth(list2tree('[3,9,20,null,null,15,7]'))
    2
    """
    def minDepth(self, root: TreeNode) -> int:
        self.min_level = float('inf')
        if not root:
            return 0

        def recur(tree, level=1):
            if not tree:
                return
            if not(tree.left or tree.right):
                if level < self.min_level:
                    self.min_level = level
                return
            else:
                recur(tree.left, level + 1)
                recur(tree.right, level + 1)


        recur(root)
        return self.min_level

