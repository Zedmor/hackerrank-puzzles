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

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #Step1: Traverse tree
        #Step2: Put items to p-queue
        #Step3: Pop k-th element

        # import queue
        from queue import PriorityQueue
        Q = PriorityQueue()


        def traverse(root):
            Q.put(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(root)

        for i in range(k):
            result = Q.get()
        return result


a = Solution()
# trlst = '[5,4,8,11,None,13,4,7,2,None,None,5,1]'
# trlst = '[1,-2,-3,1,3,-2,null,-1]'
# trlst = '[1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]'
trlst = '[1]'
tree = list2tree(trlst)
print(a.kthSmallest(tree, 1))