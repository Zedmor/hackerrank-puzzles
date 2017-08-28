# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.
#
# Subscribe to see which companies asked this question

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postorder(tree, counter, globalcounter):
            if tree != None:
                globalcounter = postorder(tree.left, counter +1, globalcounter)
                globalcounter = postorder(tree.right, counter +1, globalcounter)
                if globalcounter < counter:
                    globalcounter = counter
            return globalcounter


        if root:
            globalcounter = postorder(root, 1, 1)
            return globalcounter
        else:
            return 0

root = TreeNode(6)
a = Solution()
print(a.maxDepth(root))