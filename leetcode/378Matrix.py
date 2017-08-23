"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ? k ? n2.
"""


class Solution(object):
    class Heap(object):
        def __init__(self):
            self.heap = [None]

        def __str__(self):
            return self.heap.__str__()

        def push(self, n):
            self.heap.append(n)
            if len(self.heap) > 1:
                parent = int(len(self.heap) / 2)
                child = len(self.heap) - 1
                while parent > 0 and self.heap[parent] > self.heap[child]:
                    self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                    child = parent
                    parent = int(parent / 2)

        def minchild(self, n):
            if n * 2 + 1 >= len(self.heap):
                return n * 2
            return n * 2 if self.heap[n * 2] < self.heap[n * 2 + 1] else n * 2 + 1

        def pop(self):
            if len(self.heap) == 1:
                return None
            toreturn = self.heap[1]
            if len(self.heap) == 2:
                return self.heap.pop()
            self.heap[1] = self.heap.pop()
            parent = 1
            target = self.minchild(parent)
            while target < len(self.heap) and self.heap[parent] > self.heap[target]:
                self.heap[target], self.heap[parent] = self.heap[parent], self.heap[target]
                parent = target
                target = self.minchild(parent)
            return toreturn


    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = self.Heap()
        for i,num in enumerate(matrix[0]):
            heap.push((num,0,i))
        for i in range(k):
            root = heap.pop()
            if root[1] < len(matrix)-1:
                heap.push((matrix[root[1]+1][root[2]], root[1]+1, root[2]))
        return root[0]


a = Solution()

matrix = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]

k = 7

1, 2, 3
4, 5, 7
6, 8, 9

print(a.kthSmallest(matrix, k))
