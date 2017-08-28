"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

def Generator():
    '''
    Will generate sequence like 0,0,1,1,1,1,2,2,2,2,2
    :return:
    '''

treearr = [3, 9, 20, None, None, 15, 7]
root = TreeNode(treearr.pop(0))
for order, element in enumerate(treearr):


print(Solution().levelOrder(tree))
