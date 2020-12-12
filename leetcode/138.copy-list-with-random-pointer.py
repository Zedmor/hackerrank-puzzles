#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (34.03%)
# Total Accepted:    460.3K
# Total Submissions: 1.2M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
#
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
#
#
# Constraints:
#
#
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# The number of nodes will not exceed 1000.
#
#
#
"""
# Definition for a Node.

"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        lookup = {}
        cursor = head
        new_cursor = Node(cursor.val)
        new_head = new_cursor
        while cursor.next:
            if cursor.random:
                lookup[cursor.random.val] = Node(cursor.random.val)
            cursor = cursor.next
            if cursor.val in lookup:
                new_cursor.next = lookup.pop(cursor.val)
            else:
                node = Node(cursor.val)
                lookup[cursor.val] = node
                new_cursor.next = node

            new_cursor = new_cursor.next

        return new_head








