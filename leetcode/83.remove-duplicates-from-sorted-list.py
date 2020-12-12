#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (44.69%)
# Total Accepted:    443K
# Total Submissions: 988.2K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cursor1 = head
        cursor2 = head.next
        while cursor2:
            while cursor2 and cursor1.val == cursor2.val:
                cursor2 = cursor2.next

            cursor1.next = cursor2
            cursor1 = cursor2
            if cursor1:
                cursor2 = cursor1.next
        return head

a = [1,1,2,3,3]
cur = ListNode(a[0])
head = cur

for e in a[1:]:
    new_el = ListNode(e)
    cur.next = new_el
    cur = cur.next

nh = Solution().deleteDuplicates(None)
print(nh)
