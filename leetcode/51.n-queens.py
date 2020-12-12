#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (41.65%)
# Total Accepted:    188.1K
# Total Submissions: 421.3K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# Example:
#
#
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
#
#
#
from copy import copy
from pprint import pprint
from typing import List

class Solution:
    """
    >>> Solution().solveNQueens(4)
    ⁠[".Q..",
    "...Q",
    "Q...",
    "..Q."],
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        placements = []

        def print_solution(board):
            result = []
            for pos in board:
                target = ['.'] * n
                target[pos] = 'Q'
                result.append(''.join(target))
            return result

        def place(queen, row, board):
            for i in range(queen):
                if board[i] == row or abs(board[i] - row) == abs(i - queen):
                    return False
            return True

        def recursive(queen, board):
            for i in range(n):
                if place(queen, i, board):
                    board[queen] = i
                    if queen == n - 1:
                        placements.append(board)
                        return
                    else:
                        recursive(queen + 1, copy(board))
        recursive(0, [None] * n)
        placements = [print_solution(p) for p in placements]
        return placements

