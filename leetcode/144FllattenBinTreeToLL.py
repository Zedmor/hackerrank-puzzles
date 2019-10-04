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
        return self.val


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
                current = to_visit.pop(0)
                if current.left:
                    to_visit.append(current.left)
                if current.right:
                    to_visit.append(current.right)
                if not to_visit:
                    return current

        cursor = root

        while cursor and (cursor.left or cursor.right):
            if cursor.left:
                temp = cursor.right
                cursor.right = cursor.left
                cursor.left = None
                bfs(cursor.right).right = temp
            cursor = cursor.right


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

