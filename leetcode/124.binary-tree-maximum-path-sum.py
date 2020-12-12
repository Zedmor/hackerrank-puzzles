#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (33.52%)
# Total Accepted:    348K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
#         1
#        / \
#       2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# Output: 42
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache

#
from leetcode.treetools import TreeNode, list2tree

class Solution:
    """
    >>> Solution().maxPathSum(list2tree("[-622,-37,90,567,-516,832,-487,-59,953,null,436,-174,130,null,-330,null,253,-211,-648,null,null,-524,null,-428,-245,717,-742,null,null,null,null,null,null,null,null,731,-406,-357,-616,-810,-191,615,327,223,-506,-113,558,743,699,824,null,-727,285,-914,null,null,481,-477,786,null,null,394,null,-225,null,null,235,-309,null,2,-362,208,null,null,202,null,null,-164,211,506,-450,-581,null,null,-522,-867,-140,93,-593,-483,969,354,-148,null,null,null,-921,-738,null,null,-45,-570,null,null,546,-421,-112,null,null,null,null,616,null,466,744,740,36,-218,993,935,-719,-293,-555,null,331,616,null,-961,529,null,null,null,-368,null,82,null,-17,null,null,null,null,493,-741,null,null,-973,-694,412,null,-511,null,-678,121,null,-985,null,-270,null,null,null,null,null,83,-802,null,-538,null,null,null,-538,674,null,64,-623,null,null,279,null,null,null,null,null,null,-43,null,331,229,937,-669,null,-608,-185,null,null,-879,-115,328,-966,null,null,null,-60,null,null,null,766,-63,645,null,-657,-848,null,null,null,null,-894,null,239,null,255,120,null,-91,null,934,null,null,null,-393,null,null,null,null,null,null,542,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,305,53,null,-660,null,null,null,245,null,null,null,-200,904,null,null,null,-959,null,590,759,null,-518,null,null,null,-868]"))
    3330


    >>> Solution().maxPathSum(list2tree("[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]"))
    16

    >>> Solution().maxPathSum(list2tree("[5,4,8,11,null,13,4,7,2,null,null,null,1]"))
    48

    >>> Solution().maxPathSum(list2tree("[1,2]"))
    3

    >>> Solution().maxPathSum(list2tree("[1,2,3]"))
    6

    >>> Solution().maxPathSum(list2tree("[-10,9,20,null,null,15,7]"))
    42

    """

    # @lru_cache(None)

    def __init__(self):
        self.max_sum = -float('inf')
        self.cache = {}

    def maxPathSum(self, root: TreeNode) -> int:

        def helper(tree):
            if not tree:
                return 0

            left_result = self.cache.get(tree.left, helper(tree.left))
            self.cache[tree.left] = left_result

            right_result = self.cache.get(tree.right, helper(tree.right))
            self.cache[tree.right] = right_result

            self.max_sum = max(self.max_sum, left_result +
                               right_result + tree.val)
            return max(0, tree.val + max(left_result, right_result))

        helper(root)
        return int(self.max_sum)
