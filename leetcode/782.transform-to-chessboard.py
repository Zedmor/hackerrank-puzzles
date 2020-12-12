#
# @lc app=leetcode id=782 lang=python3
#
# [782] Transform to Chessboard
#
# https://leetcode.com/problems/transform-to-chessboard/description/
#
# algorithms
# Hard (46.76%)
# Total Accepted:    6.2K
# Total Submissions: 13.2K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]'
#
# An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows
# with each other, or any 2 columns with each other.
#
# What is the minimum number of moves to transform the board into a
# "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If
# the task is impossible, return -1.
#
#
# Examples:
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation:
# One potential sequence of moves is shown below, from left to right:
#
# 0110     1010     1010
# 0110 --> 1010 --> 0101
# 1001     0101     1010
# 1001     0101     0101
#
# The first move swaps the first and second column.
# The second move swaps the second and third row.
#
#
# Input: board = [[0, 1], [1, 0]]
# Output: 0
# Explanation:
# Also note that the board with 0 in the top left corner,
# 01
# 10
#
# is also a valid chessboard.
#
# Input: board = [[1, 0], [1, 0]]
# Output: -1
# Explanation:
# No matter what sequence of moves you make, you cannot end with a valid
# chessboard.
#
#
# Note:
#
#
# board will have the same number of rows and columns, a number in the range
# [2, 30].
# board[i][j] will be only 0s or 1s.
#
#
#
from collections import defaultdict
from typing import List


def is_it_chessboard(board):
    """
    >>> is_it_chessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]])
    False

    >>> is_it_chessboard([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    True

    """
    collector = defaultdict(set)
    for i in range(len(board)):
        for j in range(len(board[0])):
            collector[i - j].add(board[i][j])
            if len(collector[i-j]) > 1:
                return False
    return True


def swap_columns(board, col1, col2):
    """
    >>> swap_columns([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]], 0, 1)
    [[1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 0, 1]]

    """
    for i in range(len(board)):
        board[i][col1], board[i][col2] = board[i][col2], board[i][col1]
    return board


def swap_rows(board, row1, row2):
    """
    >>> swap_rows([[1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 0, 1]], 0, 1)
    [[1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 1, 0, 1]]

    """
    board[row1], board[row2] = board[row2], board[row1]
    return board

def tupleize(board):
    return tuple([tuple(r) for r in board])

class Solution:
    """
    >>> Solution().movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]])
    2

    >>> Solution().movesToChessboard([[0, 1], [1, 0]])
    0

    >>> Solution().movesToChessboard([[1, 0], [1, 0]])
    -1

    """
    def __init__(self):
        self.visited = set()

    def movesToChessboard(self, board: List[List[int]], depth=0) -> int:
        if is_it_chessboard(board):
            return depth

        results = []
        for i in range(len(board)):
            for j in range(len(board)):
                for n in range(len(board[0])):
                    for m in range(len(board[0])):
                        new_board = swap_columns(swap_rows(board, i, j), n, m)
                        if tupleize(new_board) not in self.visited:
                            self.visited.add(tupleize(new_board))
                            results.append(self.movesToChessboard(new_board, depth + 1))
        results = [r for r in results if r != -1]
        if results:
            return min(results)
        return -1




