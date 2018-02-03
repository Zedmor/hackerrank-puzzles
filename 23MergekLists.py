# Definition for singly-linked list.

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


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


class MinHeap(object):
    def __init__(self, list_of_tuples):
        self.heapList = [0]
        self.currentSize = 0
        for el in list_of_tuples:
            self.insert(el)

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def pop(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pointers = [head for head in lists]
        result = None
        result_head = result
        all_pointers_values = [(v.val, i) for i, v in enumerate(pointers) if v]
        pointers_heap = MinHeap(all_pointers_values)

        while pointers_heap.currentSize > 0:
            if all_pointers_values:
                min_val = pointers_heap.pop()
                if not result:
                    result = ListNode(pointers[min_val[1]].val)
                    result_head = result
                else:
                    result.next = ListNode(pointers[min_val[1]].val)
                    result = result.next
                pointers[min_val[1]] = pointers[min_val[1]].next
                if pointers[min_val[1]]:
                    pointers_heap.insert((pointers[min_val[1]].val, min_val[1]))
            else:
                break

        return result_head




def make_ll(param):
    head = ListNode(param.pop(0))
    cursor = head
    for val in param:
        cursor.next = ListNode(val)
        cursor = cursor.next
    return head


list1 = make_ll([1, 2, 3, 7, 8])
print(list1)
list2 = make_ll([4, 5, 6])
print(list2)

print(Solution().mergeKLists([list1, list2]))
