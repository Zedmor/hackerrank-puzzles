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

        def swap(node, counter):
            if node and node.next and counter > 0:
                # node.next, node2.next = node2.next, node.next
                listhead = node
                for i in range(counter):
                    head = node.next

                head.next = swap(head, counter - 1)
                return listhead
                # backup = node
                # node.next = swap(node.next, counter-1)
                # node.next = backup
                # return node
                # node.next = swap(node.next, counter - 1)
                # return node
                # nodex.next, node.next = node.next, nodex.next
                # node2.next = node
                # swap(node2 , node2.next, counter-1)
            if counter == 0:
                backup = node
                # node.next =
                return node.next

                # if node:
                #     return None

                # pointers = [0] * k
                # backup = head
                # head = swap(head, k-1)
                # print(head)


                # pointers[i] = head.next

        # print(pointers)
        while k > 0:
            pointer = head
            for i in range(k):
                pointer = pointer.next


            printlist(head)


def createlist(array):
    list = None
    array = array
    for element in reversed(array):
        if list:
            new_node = ListNode(element, list)
            # new_node.next = list
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

list = createlist([1, 2, 3, 4, 5, 6, 7])
# printlist(list)
print(a.reverseKGroup(list, 5))
