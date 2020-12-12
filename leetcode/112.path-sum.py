#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (40.31%)
# Total Accepted:    450.7K
# Total Submissions: 1.1M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    >>> Solution().hasPathSum(list2tree('[5,4,8,11,null,13,4,7,2,null,null,null,1]'), 22)
    True
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def recur(tree, total=0):
            if tree:
                total += tree.val
                if not(tree.left or tree.right) and total == sum:
                    return True
                if recur(tree.left, total) or recur(tree.right, total):
                    return True

        return recur(root)


