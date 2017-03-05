"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            outerlist, innerlist = (l1, l2) if l1.val < l2.val else (l2, l1)
            head = outerlist
            while innerlist:
                while outerlist.next and outerlist.next.val < innerlist.val:
                    outerlist = outerlist.next
                temppointer = outerlist.next
                outerlist.next = ListNode(innerlist.val)
                outerlist.next.next = temppointer

                innerlist = innerlist.next

            return head
        else:
            if l1:
                return l1
            else:
                return l2


l1 = ListNode(2)
l2 = ListNode(1)

a = Solution()
z = a.mergeTwoLists(l1, l2)
print(z)