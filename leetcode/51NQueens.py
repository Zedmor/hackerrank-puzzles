# uses Python3
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
# both indicate a queen and an empty space respectively.
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
from copy import deepcopy


def placement_possible(board, i, j):
    return board[i][j] == '.'


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = set()
        initial_board = [['.' for x in range(n)] for y in range(n)]

        def recur_search(board, deep=0):
            if deep == n:
                counter = 0
                for row in board:
                    counter += row.count('Q')
                if counter == n:
                    solutions.add(tuple(tuple(row) for row in board))
                return
            for i in range(n):
                for j in range(n):
                    if placement_possible(board, i, j):
                        candidate = deepcopy(board)
                        for m in range(n):
                            candidate[i][m] = 'x'
                            candidate[m][j] = 'x'
                        new_i, new_j = i, j
                        while new_i >= 0 and new_j >= 0:
                            candidate[new_i][new_j] = 'x'
                            new_i -= 1
                            new_j -= 1
                        new_i, new_j = i, j
                        while new_i < n and new_j < n:
                            candidate[new_i][new_j] = 'x'
                            new_j += 1
                            new_i += 1
                        new_i, new_j = i, j
                        while new_i >= 0 and new_j < n:
                            candidate[new_i][new_j] = 'x'
                            new_j += 1
                            new_i -= 1
                        new_i, new_j = i, j
                        while new_i < n and new_j >= 0:
                            candidate[new_i][new_j] = 'x'
                            new_j -= 1
                            new_i += 1
                        candidate[i][j] = 'Q'
                        recur_search(candidate, deep + 1)

        recur_search(initial_board)
        solutions = [[''.join(row).replace('x', '.') for row in solution] for solution in solutions]
        return solutions


a = Solution()
print(a.solveNQueens(6))
# print(a.solveNQueens(2))
