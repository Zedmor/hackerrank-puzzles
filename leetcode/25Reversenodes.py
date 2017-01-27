# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        if not next:
            self.next = None
        else:
            self.next = next

    def insert(self, data):
        new_node = ListNode(data)
        new_node.next(self.head)
        self.head = new_node


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverserecur(head, k):
            currNode = head
            nextNode = None
            prevNode = None
            iterator = 0
            while currNode and iterator < k:
                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode
                iterator += 1
            if not currNode and iterator < k:
                # разверни и верни!
                head.next = nextNode
                head = prevNode
                return reverserecur(head, iterator)
            if not nextNode:
                return prevNode
            head.next = reverserecur(nextNode, k)
            head = prevNode
            return head
        if head:
            return reverserecur(head, k)



def createlist(array):
    list = None
    array = array
    for element in reversed(array):
        if list:
            new_node = ListNode(element, list)
            list = new_node
        else:
            list = ListNode(element)
    return list


def printlist(head):
    while head:
        if head.val:
            print(head.val)
        head = head.next


a = Solution()

list = createlist([1,2,3,4,5])
# printlist(list)
print(a.reverseKGroup(list, 2))
