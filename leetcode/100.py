# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            if p==q:
                return True
            else:
                return False
        queue1 = [p]
        queue2 = [q]
        equality = True
        while queue1 and queue2:
            tree1 = queue1.pop()
            tree2 = queue2.pop()
            equality = tree1.val == tree2.val
            if equality:
                equality = (tree1.left==None) == (tree2.left==None)
            if equality:
                equality = (tree1.right == None) == (tree2.right == None)
            if not equality:
                break
            if tree1.left and tree2.left:
                queue1.append(tree1.left)
                queue2.append(tree2.left)
            if tree1.right and tree2.right:
                queue1.append(tree1.right)
                queue2.append(tree2.right)
        return equality


print(Solution().isSameTree(TreeNode(0), TreeNode(0)))