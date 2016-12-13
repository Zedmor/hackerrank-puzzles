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
#[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

class Solution (object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        import numpy as np
        # matrix = np.zeros(shape=(n,n))

        allsols = np.array([np.zeros(shape=(n,n))] * (n**2))
        # for sol in range(n**2):
        for i in range(n):
            for j in range(n):
                print(2**i*3**j)
                # allsols[i*j][i-1,j-1] = 1




        # return allsols

a = Solution()
print(a.solveNQueens(4))