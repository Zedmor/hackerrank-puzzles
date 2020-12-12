#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (35.38%)
# Total Accepted:    281.2K
# Total Submissions: 712.7K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#
#
#
# Definition for singly-linked list.
from leetcode.treetools import ListNode, list2ll


class Solution:
    """
    >>> Solution().reorderList(list2ll([1,2,3,4,5]))

    """

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        backup_head = head
        p1 = head
        p2 = head.next
        p3 = p2.next
        while p1 != p2:
            while p3.next:
                p3 = p3.next
                p2 = p2.next
            tmp = p1.next
            p1.next = p3
            p3.next = tmp
            p2.next = None
            p1 = p1.next.next
            while p3.next != p2:
                p3 = p3.next

        print(backup_head)


