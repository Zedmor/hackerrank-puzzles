#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (45.99%)
# Total Accepted:    337K
# Total Submissions: 727.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

# from leetcode.treetools import TreeNode, list2tree


class Solution:
    """
    >>> Solution().zigzagLevelOrder(list2tree('[3,9,20,null,null,15,7]'))
    [[3], [20,9],[15,7]]

    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def height(tree):
            if not tree:
                return 0
            else:
                lheight = height(tree.left)
                rheight = height(tree.right)

                return max(lheight, rheight) + 1

        def iterate_level(tree, level, direction):
            if not tree:
                return
            if level == 1:
                result.append(tree.val)
            elif level > 1:
                if direction:
                    iterate_level(tree.right, level - 1, direction)
                    iterate_level(tree.left, level - 1, direction)
                else:
                    iterate_level(tree.left, level - 1, direction)
                    iterate_level(tree.right, level - 1, direction)

        h = height(root)
        all_results = []
        for l in range(1, h + 1):
            result = []
            iterate_level(root, l, l % 2 == 0)
            all_results.append(result)

        return all_results

