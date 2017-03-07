"""449. Serialize and Deserialize BST Serialization is the process of
converting a data structure or object into a sequence of bits so that it can
be stored in a file or memory buffer, or transmitted across a network
connection link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize a binary search tree. There
is no restriction on how your serialization/deserialization algorithm should
work. You just need to ensure that a binary search tree can be serialized to
a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your
serialize and deserialize algorithms should be stateless. """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'v: {}, left: {}, right: {}'.format(self.val, self.left is not
                                                   None,
                                                   self.right is not None)


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        #queue = [root]
        # visited = []
        printout = []
        def recurserialize(root):
            if not root:
                printout.append('* ')
            else:
                printout.append(str(root.val)+ ' ')
                recurserialize(root.left)
                recurserialize(root.right)
        recurserialize(root)
        return ''.join(printout)[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # if data:
        #     root = TreeNode(data.pop(0))
        #     # root.val = data.pop
        if not data:
            return None
        data = data.split(' ')
        data = iter(data)

        def resucsbuild():
            try:
                val = next(data)
            except StopIteration:
                return
            if val == '*':
                return
            else:
                node = TreeNode(int(val))
                node.left = resucsbuild()
                node.right = resucsbuild()
                return node

        return resucsbuild()


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))


root = TreeNode(2)
root.right = TreeNode(1)
# root.right = TreeNode(10)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(6)
# root.left.right.left = TreeNode(4)
# root.left.right.right = TreeNode(7)
#
# root.right = TreeNode(10)
# root.right.right = TreeNode(14)
# root.right.right.left = TreeNode(13)

codec = Codec()
data = codec.serialize(root)

print('[{}]'.format(data))
root2 = codec.deserialize(data)
print('[{}]'.format(codec.serialize(root2)))

# codec.deserialize(codec.serialize())
