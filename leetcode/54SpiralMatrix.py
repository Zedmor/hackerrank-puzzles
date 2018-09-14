"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

>>> Solution().spiralOrder(\
[\
 [ 1, 2, 3 ],\
 [ 4, 5, 6 ],\
 [ 7, 8, 9 ]\
])
[1, 2, 3, 6, 9, 8, 7, 4, 5]

>>> Solution().spiralOrder(\
[\
  [1, 2, 3, 4],\
  [5, 6, 7, 8],\
  [9,10,11,12]\
])
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
>>> Solution().spiralOrder([[7],[9],[6]])
[7, 9, 6]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or type(matrix[0]) is not list:
            return []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        res = []
        while left < right and top < bottom:

            for x in range(left, right):
                res.append(matrix[top][x])
            start_y = top + 1
            y_pass = False
            for y in range(top + 1, bottom):
                y_pass = True
                res.append(matrix[y][x])
            if y_pass:
                x_pass = False
                for x in range(right - 2, left - 1, -1):
                    x_pass = True
                    res.append(matrix[y][x])
                if x_pass:
                    for y in range(bottom - 2, top, -1):
                        res.append(matrix[y][x])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res
