"""Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def bfs(root):
            """In BFS the Node Values at each level of the Tree are traversed before going to next level"""

            to_visit = []
            if root:
                to_visit.append(root)
            while to_visit:
                current = to_visit.pop()
                if current.left:
                    to_visit.append(current.left)
                if current.right:
                    to_visit.append(current.right)
                if not to_visit or not current.right:
                    return current

        cursor = root

        while cursor and (cursor.left or cursor.right):
            if cursor.left:
                temp = cursor.right
                cursor.right = cursor.left
                cursor.left = None
                right_node = bfs(cursor.right)
                right_node.right = temp
            cursor = cursor.right


root = stringToTreeNode('[7,-10,2,-4,3,-8,null,null,null,null,-1,11]')

Solution().flatten(root)


root = TreeNode(5, TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)),
                TreeNode(6))

Solution().flatten(root)

print(root)

Solution().flatten(None)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(5, None, TreeNode(6)))

Solution().flatten(root)

cursor = root
i = 1
while cursor.right:
    assert cursor.val == i
    i += 1
    cursor = cursor.right

