#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (47.10%)
# Total Accepted:    92.9K
# Total Submissions: 191.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
#
#
#
# Example:
#
#
# Input:
# [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#
#
from collections import defaultdict
from typing import List


class Solution:
    """
    >>> Solution().findDiagonalOrder([[3],[2]])
    [3, 2]

    >>> Solution().findDiagonalOrder([[2, 3]])
    [2, 3]

    >>> Solution().findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
    [1, 2, 4, 7, 5, 3, 6, 8, 9]

    """
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        n = len(matrix)
        m = len(matrix[0])
        collector = defaultdict(list)
        for i in range(n):
            for j in range(m):
                collector[i+j].append(matrix[i][j])
        result = []
        for k, v in collector.items():
            if k % 2:
                result.extend(v)
            else:
                result.extend(reversed(v))
        return result
