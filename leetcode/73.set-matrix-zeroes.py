#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (42.40%)
# Total Accepted:    300.7K
# Total Submissions: 706.1K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
#
# Example 1:
#
#
# Input:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# Example 2:
#
#
# Input:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#
from typing import List


def nullify_row(matrix, i):
    matrix[i] = [None] * len(matrix[0])


def nullify_col(matrix, j):
    for row in matrix:
        row[j] = None if row[j] != 0 else 0


class Solution:
    """
    >>> Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])


    >>> Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])
    [[1,0,1],[0,0,0],[1,0,1]]

    >>> Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            should_null_row = False
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    nullify_col(matrix, j)
                    should_null_row = True
            if should_null_row:
                nullify_row(matrix, i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
        # return matrix


