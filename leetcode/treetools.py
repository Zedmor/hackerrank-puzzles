# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'TreeNode(v: {self.val}, left: {self.left}, right: {self.right})'


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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2ll(array_repr):
    if array_repr:
        ln = ListNode(array_repr[0])
    else:
        return

    head = ln

    for el in array_repr[1:]:
        new_node = ListNode(el)
        ln.next = new_node
        ln = new_node

    return head
