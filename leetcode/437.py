"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        visited = {}
        queue = [root]
        def DFS(root, path=None):
            if not path:
                path = [root.val]
            else:
                path.append(root.val)
            # while sum(path) > target_sum:
            #     path.pop(0)

            print(path)
            if root.left:
                DFS(root.left, path)
            if root.right:
                DFS(root.right, path)
            path.pop()


        DFS(root)






root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)

root.left.left.right = TreeNode(-2)
root.left.left.left  = TreeNode(3)


print(Solution().pathSum(root, 8))




