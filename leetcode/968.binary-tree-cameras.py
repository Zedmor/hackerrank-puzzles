#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (35.84%)
# Total Accepted:    10.9K
# Total Submissions: 30.4K
# Testcase Example:  '[0,0,null,0,0]'
#
# Given a binary tree, we install cameras on the nodes of the tree. 
#
# Each camera at a node can monitor its parent, itself, and its immediate
# children.
#
# Calculate the minimum number of cameras needed to monitor all nodes of the
# tree.
#
#
#
# Example 1:
#
#
#
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
#
# Example 2:
#
#
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
#
#
#
# Note:
#
#
# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.
#
#
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from copy import copy
from itertools import count


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    def minCameraCover(self, root: TreeNode) -> int:
        def add_name(node):
            if not hasattr(node, 'name'):
                node.name = next(counter)

        if not root.left and not root.right:
            return 1

        visited = set()
        counter = count()
        dict_form = defaultdict(set)
        to_visit = [root]
        while to_visit:
            cur = to_visit.pop()
            add_name(cur)
            visited.add(cur)
            if cur.left and cur.left not in visited:
                add_name(cur.left)
                to_visit.append(cur.left)
                dict_form[cur.name].add(cur.left.name)
                dict_form[cur.left.name].add(cur.name)
            if cur.right and cur.right not in visited:
                add_name(cur.right)
                to_visit.append(cur.right)
                dict_form[cur.name].add(cur.right.name)
                dict_form[cur.right.name].add(cur.name)



        cameras = set()
        new_cameras = set()
        covered = set()
        while dict_form:
            covered = covered.union(*[v for k, v in dict_form.items() if k in new_cameras]).union(cameras)

            for el in new_cameras:
                if el in dict_form:
                    del dict_form[el]
                for v in dict_form.values():
                    v.discard(el)
            for key in copy(dict_form):
                if len(dict_form[key]) == 0:
                    del dict_form[key]

            end_nodes = set([k for k, v in dict_form.items() if len(v) == 1 and k not in covered])

            if not end_nodes:
                try:
                    to_remove = next(k for k, v in dict_form.items() if len(v) == 1)
                    del dict_form[to_remove]
                    for k, node in copy(dict_form).items():
                        dict_form[k].discard(to_remove)
                except StopIteration:
                    break
            new_cameras = set()
            while end_nodes:
                node = end_nodes.pop()
                place = next(iter(dict_form[node]))
                cameras.add(place)
                new_cameras.add(place)
                for node in copy(end_nodes):
                    if node == place or place in dict_form[node]:
                        end_nodes.discard(node)



        return len(cameras)


# t = stringToTreeNode('[0,0,null,0,0]')
# print(Solution().minCameraCover(t))
#
# t = stringToTreeNode('[0,0,null,0,null,0,null,null,0]')
# print(Solution().minCameraCover(t))
# t = stringToTreeNode('[0]')
# print(Solution().minCameraCover(t))
# t = stringToTreeNode('[0,0,0,null,0,null,null,0,null,null,0,0]')
# print(Solution().minCameraCover(t))


# t = stringToTreeNode('[0,0,null,null,0,0,null,null,0,0]')
# print(Solution().minCameraCover(t))

t = stringToTreeNode('[0,0,0,null,0,null,null,0,null,null,0,0]')
print(Solution().minCameraCover(t))

# t = stringToTreeNode( '[0,null,0]')
# print(Solution().minCameraCover(t))
