"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
>>> Solution().rotateRight(make_list([0, 1, 2]), 4).val
2


>>> Solution().rotateRight(make_list([1, 2, 3, 4, 5]), 2).val
4

>>> Solution().rotateRight(make_list([1, 2]), 0).val
1

>>> Solution().rotateRight(make_list([1, 2]), 2).val
1


#
# >>> Solution().rotateRight(make_list([1, 2, 3]), 2000000000).val
# 4
#
>>> Solution().rotateRight(make_list([1, 2]), 1).val
2



>>> Solution().rotateRight(make_list([0, 1, 2]), 10).val
2

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def make_list(array_repr):
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


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return head

        stack_of_nodes = []

        cursor = head
        while cursor is not None:
            stack_of_nodes.append(cursor)
            cursor = cursor.next

        new_start_index = len(stack_of_nodes) - k % len(stack_of_nodes)
        if new_start_index == len(stack_of_nodes):
            new_start_index = 0
        new_start = stack_of_nodes[new_start_index]

        if new_start_index - 1 == len(stack_of_nodes):
            new_end = stack_of_nodes[0]
        else:
            new_end = stack_of_nodes[new_start_index - 1]

        stack_of_nodes[-1].next = head

        new_end.next = None

        return new_start



