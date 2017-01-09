# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        #Find node
        node = root
        while node.val is not key:
            if key < node.val and node.left:
                parent = node
                node = node.left
            elif node.right:
                parent = node
                node = node.right
            else:
                print('no such node')
                break

        print(node.val)
        if not (node.left and node.right):
            node = None

        return root

def treeArrayToBST(array):
    count = 0
    queue = []
    root = TreeNode(array[0])
    queue.append(root)
    cur = None
    for i in range(1, len(array)):
        node = TreeNode(array[i])
        if count == 0:
            cur = queue.pop(0)
        if count == 0:
            count += 1
            cur.left = node
        else:
            count = 0
            cur.right = node
        if array[i]:
            queue.append(node)
    return root


a = Solution()
root = [5, 3, 6, 2, 4, None, 7]
BST = treeArrayToBST(root)
key = 4
newBST = a.deleteNode(BST, key)
print(newBST)
