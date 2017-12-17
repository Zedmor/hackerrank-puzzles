# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        repr = ""
        cursor = self
        while cursor:
            repr += str(cursor.val) + " -> "
            cursor = cursor.next
        repr += "Nil"
        return repr




class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cursor = head
        previous = None
        if cursor.next:
            cursor2 = cursor.next
        else:
            return head

        while cursor and cursor.next:
            if cursor.val == cursor2.val:
                while cursor2 and cursor2.val == cursor.val:
                    cursor2 = cursor2.next
                if previous:
                    previous.next = cursor2
                else:
                #     previous = cursor2
                    head = cursor2
                cursor = cursor2
                if cursor2 and cursor2.next:
                    cursor2 = cursor2.next
            else:
                previous = cursor
                cursor = cursor.next
                cursor2 = cursor.next
        return head


nodes = [1,1]

cursor = ListNode(nodes.pop(0))
head = cursor

while nodes:
    cursor.next = ListNode(nodes.pop(0))
    cursor = cursor.next

print(Solution().deleteDuplicates(head))
