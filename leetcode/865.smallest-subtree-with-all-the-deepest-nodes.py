#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (60.30%)
# Total Accepted:    46.9K
# Total Submissions: 76.6K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given the root of a binary tree, the depth of each node is the shortest
# distance to the root.
#
# Return the smallest subtree such that it contains all the deepest nodes in
# the original tree.
#
# A node is called the deepest if it has the largest depth possible among any
# node in the entire tree.
#
# The subtree of a node is tree consisting of that node, plus the set of all
# descendants of that node.
#
# Note: This question is the same as 1123:
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the
# diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2
# is the smallest subtree among them, so we return it.
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
#
#
# Example 3:
#
#
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the
# subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
#
#
#
# Definition for a binary tree node.
# from leetcode.treetools import list2tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val

def all_same(items):
    return all(x == items[0] for x in items)

class Solution:
    """
    >>> Solution().subtreeWithAllDeepest(list2tree('[1]'))
    [1]

    >>> Solution().subtreeWithAllDeepest(list2tree('[3,5,1,6,2,0,8,null,null,7,4]'))
    [2, 7, 4]

    >>> Solution().subtreeWithAllDeepest(list2tree('[0,1,3,null,2]'))
    [2]

    """

    def __init__(self):
        self.max_len = 0
        self.path_container = []

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, path=None):
            if not path:
                path = []
            if not node:
                return
            if not node or not (node.left or node.right):
                return path + [node]
            for new_node in (node.left, node.right):
                res = dfs(new_node, path + [node])
                if res:
                    if len(res) > self.max_len:
                        self.max_len = len(res)
                        self.path_container = []
                        self.path_container.append(res)
                    elif len(res) == self.max_len:
                        self.path_container.append(res)

        dfs(root)
        last_level = root
        for level in zip(*self.path_container):
            if all_same(level):
                last_level = level[0]
            else:
                break
        return last_level

