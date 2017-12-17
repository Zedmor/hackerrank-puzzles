# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        stack = [root]
        result = []
        self.level_values = defaultdict(list)
        self.recurDFS(stack, 0)
        for level in sorted(self.level_values.keys()):
            result.append(float(sum(self.level_values[level])) / float(len(self.level_values[level])))
        return result

    def recurDFS(self, queue, depth):
        if queue:
            node = queue.pop()
        else:
            return
        self.level_values[depth].append(node.val)
        if node.left:
            queue.insert(0, node.left)
            self.recurDFS(queue, depth + 1)
        if node.right:
            queue.insert(0, node.right)
            self.recurDFS(queue, depth + 1)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().averageOfLevels(root))
