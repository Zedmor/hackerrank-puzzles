"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

>>> Solution().generateMatrix(1)
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
from itertools import cycle
from pprint import pprint


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for x in range(n)] for y in range(n)]
        counter = 1
        cursor = (0, 0)
        next_el = 0

        all_directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])

        direction = next(all_directions)

        while next_el == 0:
            matrix[cursor[0]][cursor[1]] = counter
            counter += 1
            next_coord = [sum(x) for x in zip(cursor, direction)]
            if next_coord[0] >= n or next_coord[0] < 0 or next_coord[1] >= n or next_coord[1] < 0 or matrix[
                next_coord[0]][next_coord[1]] != 0:
                direction = next(all_directions)
                next_coord = [sum(x) for x in zip(cursor, direction)]
            try:
                next_el = matrix[next_coord[0]][next_coord[1]]
            except IndexError:
                next_el = matrix[0][0]
            cursor = next_coord



        return matrix
