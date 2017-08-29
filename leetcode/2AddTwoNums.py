# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryover1 = 0
        carryover2 = 0
        head1 = l1
        head2 = l2
        leadhead = head1
        head1val = None
        while True:
            if head1:
                result = l1
            else:
                result = l2
            if head1:
                head1val = head1.val
                head1.val += (head2.val if head2 else 0) + carryover1
                carryover1 = 0
                if head1.val > 9:
                    head1.val = head1.val % 10
                    carryover1 = 1
                if not head1.next:
                    if carryover1:
                        head1.next = ListNode(1)
                        head1.val = head1.val % 10

                    head1 = None
                else:
                    head1 = head1.next
            if head2:
                head2.val += (head1val if head1val else 0) + carryover2
                head1val = None
                carryover2 = 0
                if head2.val > 9:
                    head2.val = head2.val % 10
                    carryover2 = 1
                if not head2.next:
                    if carryover2:
                        head2.next = ListNode(1)
                        head2.val = head2.val % 10
                    head2 = None
                else:
                    head2 = head2.next

            if not head1 and not head2:
                return result


def list2ll(lst):
    lst.reverse()
    a = ListNode(lst.pop())
    head = a
    while lst:
        nxt = ListNode(lst.pop())
        a.next = nxt
        a = nxt
    return head


# l1 = list2ll([1, 8])
# l2 = list2ll([0])

l1 = list2ll([5])
l2 = list2ll([5])

print(Solution().addTwoNumbers(l1, l2))
