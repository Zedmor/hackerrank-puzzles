"""
Partition List
Difficulty:Medium

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        old_head = head
        greater_list_origin = None
        greater_list = None
        if not old_head:
            return
        while head and head.val >= x:
            if not greater_list:
                greater_list = old_head
                greater_list_origin = greater_list
            else:
                greater_list.next = head
                greater_list = greater_list.next
            head = head.next
            old_head = head
        if not head:
            return greater_list_origin
        while head.next:
            if head.next:
                if head.next.val < x:
                    head = head.next
                else:
                    if not greater_list:
                        greater_list_origin = ListNode(head.next.val)
                        greater_list = greater_list_origin
                        head.next = head.next.next
                    else:
                        greater_list.next = head.next
                        greater_list = greater_list.next
                        head.next = head.next.next
        if greater_list:
            greater_list.next = None
        if old_head and greater_list:
            head.next = greater_list_origin
        return old_head


head = ListNode(1)
true_head = head
for val in [4, 3, 2, 5, 2]:
    head.next = ListNode(val)
    head = head.next

m = Solution().partition(true_head, 3)
print(m)
