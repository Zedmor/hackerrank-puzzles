"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        cursor = self
        repr = ''
        while cursor:
            repr += str(cursor.val) + (' -> ' if cursor.next else '')
            cursor = cursor.next
        return repr


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            cursor = head
            next_item = cursor.next
            tmp = next_item.next
            next_item.next = cursor
            cursor.next = tmp
            head = next_item
            cursor = head.next
            while cursor.next and cursor.next.next:
                item1 = cursor.next
                item2 = cursor.next.next
                outpointer = cursor.next.next.next
                cursor.next = item2
                item2.next = item1
                item1.next = outpointer
                cursor = item1

        return head


def make_ll(param):
    head = ListNode(param.pop(0))
    cursor = head
    for val in param:
        cursor.next = ListNode(val)
        cursor = cursor.next
    return head


list1 = make_ll([1, 2,3])
print(list1)


print(Solution().swapPairs(list1))
