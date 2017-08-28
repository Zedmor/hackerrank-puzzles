"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

Subscribe to see which companies asked this question.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def xy(z):
            if len(matrix) > 1:
                y = z//(len(matrix[0]))
                return y,  z-(y*(len(matrix[0])))
            else:
                return 0, z

        # for i in range(len(matrix)*len(matrix[0])):
        #     print(xy(i))
        if not matrix or not matrix[0]:
            return False
        if type(matrix[0]) is int:
            matrix = list([matrix])
        left = 0
        right = len(matrix)*len(matrix[0])
        mid = (right - left) // 2 + left
        xym = xy(mid)
        while not (right == mid or left == mid) or matrix[xym[0]][xym[1]] == target:
            if matrix[xym[0]][xym[1]] == target:
                return True
            if matrix[xym[0]][xym[1]] > target:
                right = mid
            if matrix[xym[0]][xym[1]] < target:
                left = mid
            mid = (right-left)//2+left
            xym = xy(mid)
        # print(left, mid, right)
        return False

a = Solution()
# A = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
# A = [1,3,5,6]
A = [[1], [3]]
x = 1
print(a.searchMatrix(A, x))
