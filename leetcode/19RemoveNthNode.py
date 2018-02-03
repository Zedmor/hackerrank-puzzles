"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val) + (' -> ' if self.next else '')


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        list_pointer = {}
        cursor = head
        while cursor:
            list_pointer[i] = cursor
            i += 1
            cursor = cursor.next
        if i - n < 0:
            return None
        elif i - n == 0:
            head = head.next
        elif i - n + 1 >= i:
            # head = list_pointer[i-n-1].next
            list_pointer[i - n - 1].next = None
        else:
            list_pointer[i - n - 1].next = list_pointer[i - n + 1]
        return head


head = ListNode(1)
cursor = head

for i in range(2, 3):
    cursor.next = ListNode(i)
    cursor = cursor.next


def print_linked_list(lilist):
    cursor = lilist
    while cursor:
        print(cursor, end='')
        cursor = cursor.next
    print()


print_linked_list(head)

print_linked_list(Solution().removeNthFromEnd(head, 2))
