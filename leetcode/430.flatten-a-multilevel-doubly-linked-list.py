#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
#
# algorithms
# Medium (50.71%)
# Total Accepted:    126.1K
# Total Submissions: 225.6K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]'
#
# You are given a doubly linked list which in addition to the next and previous
# pointers, it could have a child pointer, which may or may not point to a
# separate doubly linked list. These child lists may have one or more children
# of their own, and so on, to produce a multilevel data structure, as shown in
# the example below.
#
# Flatten the list so that all the nodes appear in a single-level, doubly
# linked list. You are given the head of the first level of the list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:
#
# The multilevel linked list in the input is as follows:
#
#
#
# After flattening the multilevel linked list it becomes:
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:
#
# The input multilevel linked list is as follows:
#
#  1---2---NULL
#  |
#  3---NULL
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
#
# How multilevel linked list is represented in test case:
#
# We use the multilevel linked list from Example 1 above:
#
#
# 1---2---3---4---5---6--NULL
#         |
#         7---8---9---10--NULL
#             |
#             11--12--NULL
#
# The serialization of each level is as follows:
#
#
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
#
#
# To serialize all levels together we will add nulls in each level to signify
# no node connects to the upper node of the previous level. The serialization
# becomes:
#
#
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
#
#
# Merging the serialization of each level and removing trailing nulls we
# obtain:
#
#
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
#
#
# Constraints:
#
#
# Number of Nodes will not exceed 1000.
# 1 <= Node.val <= 10^5
#
#
#

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __repr__(self):
        return f'{self.val}'


def parse_from_list(s):

    inp = s.replace('[', '')
    inp = inp.replace(']', '')
    inp = inp.split(',')
    inp = [int(e) if e not in ('null', '') else None for e in inp]

    prv = None
    main_head = None
    head = None
    while inp:
        el = inp.pop(0)
        if el is not None:
            node = Node(el, prv, None, None)
            if prv:
                prv.next = node
                node.prev = prv
            else:
                if not head:
                    head = node
                if not main_head:
                    main_head = head
            prv = node
        else:
            cursor = head
            while inp and el is None:
                el = inp.pop(0)
                if not el:
                    cursor = cursor.next
            if el is not None:
                cursor.child = Node(el, None, None, None)
                prv = cursor.child
                head = prv

    return main_head


class Solution:
    """
    >>> Solution().flatten(parse_from_list('[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]'))
    [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

    >>> Solution().flatten(parse_from_list('[]'))
    []

    """
    def flatten(self, head):

        def _flatten(node):
            if not node:
                return None, None
            cursor = node
            while cursor.next or cursor.child:
                if not cursor.child:
                    cursor = cursor.next
                else:
                    head, tail = _flatten(cursor.child)
                    head.prev = cursor
                    cursor.child = None
                    if cursor.next:
                        cursor.next.prev = tail
                    tail.next = cursor.next
                    cursor.next = head
                    cursor = tail
            return node, cursor
        _flatten(head)

        return head

