# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list2tree(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' or val == 'None' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def tree2list(treeobject):
    def serializeHelper(node):
        if not node:
            vals.append(None)
        else:

            if node.val or node.left or node.right: vals.append((node.val))
            serializeHelper(node.left)
            serializeHelper(node.right)

    vals = []
    serializeHelper(treeobject)
    while vals and vals[-1] is None:
        vals.pop()
    return vals


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        Given a binary tree and a sum, find all root-to-leaf paths where
        each path's sum equals the given sum.

        For example:
        Given the below binary tree and sum = 22,
                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \    / \
                7    2  5   1
        return
        [
           [5,4,11,2],
           [5,8,4,5]

        провести DFS. Как только сумма найдена абортировать DFS
        """

        def sumhelper(node):
            def evaluated(node):
                return (((node.left == None) or (isinstance(node.left.val, tuple))) and ((node.right == None) or isinstance(
                     node.right.val, tuple)))
            if not node:
                return
            if node.val[1] == sum and node.left == None and node.right == None:
                solution.append(node.val[0])
                node.val = (float("inf"), float("inf"))
                return True
            # try:
            # if ((node.left == None))  and ((node.right == None) or isinstance(node.right.val, tuple)):

            # if ((node.left == None) or (isinstance(node.left.val, tuple))) and ((node.right == None) or isinstance(
            #         node.right.val, tuple)):
            #     return
            # except AttributeError:
            #     pass

            if node.left:
                try:
                    leftv = node.left.val[0]
                except TypeError:
                    leftv = node.left.val
                node.left.val = (leftv, node.val[1] + leftv)
                # if not evaluated(node.left):
                if sumhelper(node.left):
                    solution.append(node.val[0])
                    return True
            if node.right:
                try:
                    rightv = node.right.val[0]
                except TypeError:
                    rightv = node.right.val
                node.right.val = (rightv, node.val[1] + rightv)
                # if not evaluated(node.right):
                if sumhelper(node.right):
                    solution.append(node.val[0])
                    return True

        globalsolution = []
        solution = []
        if root: root.val = (root.val, root.val)
        while True:
            sumhelper(root)
            if not solution:
                break
            # if globalsolution and list(reversed(solution)) == globalsolution[-1]:
            #     break
            globalsolution.append(list(reversed(solution)))
            solution = []
        return globalsolution


a = Solution()
# trlst = '[5,4,8,11,None,13,4,7,2,None,None,5,1]'
# trlst = '[1,-2,-3,1,3,-2,null,-1]'
# trlst = '[1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]'
trlst = '[0,1,1]'
tree = list2tree(trlst)
print(a.pathSum(tree, 1))
