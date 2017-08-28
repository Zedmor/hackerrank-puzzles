"""According to the Wikipedia's article: "The Game of Life, also known simply
as Life, is a cellular automaton devised by the British mathematician John
Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia
article):

1. Any live cell with fewer than two live neighbors dies, as if caused by
under-population.

2. Any live cell with two or three live neighbors lives on to
the next generation.

3. Any live cell with more than three live neighbors dies,
as if by over-population..

4. Any dead cell with exactly three live neighbors
becomes a live cell, as if by reproduction. Write a function to compute the
next state (after one update) of the board given its current state.

Follow up: Could you solve it in-place? Remember that the board needs to be
updated at the same time: You cannot update some cells first and then use
their updated values to update other cells. In this question, we represent
the board using a 2D array. In principle, the board is infinite, which would
cause problems when the active area encroaches the border of the array. How
would you address these problems? """

import logging

import numpy as np


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def num_neighbors(coords):
            """
            :param coords: (row, col)
            :return: # of neighbors
            """
            row, col = coords
            counter = 0
            for r in range(max(0, row - 1), min(len(board), row + 2)):
                for c in range(max(0, col - 1), min(len(board[0]),
                                                    col + 2)):
                    logger.debug((r, c))
                    if not (row == r and col == c) and board[r][c] > 0:
                        counter += 1

            return counter if counter > 0 else -1

        logging.basicConfig(level=logging.WARNING)
        logger = logging.getLogger()

        if not board:
            return

        if type(board[0]) == int:
            board = [board]

        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if not board[r][c]:
                    if num_neighbors((r, c)) == 3:
                        board[r][c] = -2
        logger.info(np.array(board))

        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if board[r][c] > 0:
                    board[r][c] = num_neighbors((r,
                                                 c))

        logger.info(np.array(board))
        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if 3 < board[r][c] or board[r][c] == 1:
                    board[r][c] = -1
        logger.info(np.array(board))



        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if board[r][c] > 0 or board[r][c]==-2:
                    board[r][c] = 1
                if board[r][c] == -1:
                    board[r][c] = 0
        logger.info(np.array(board))

        return


board = [[0, 0, 0, 0, 0, ],
         [0, 0, 0, 1, 0, ],
         [0, 0, 0, 0, 0, ],
         [0, 0, 0, 1, 0, ],
         [0, 0, 0, 0, 0, ],
         [0, 0, 0, 0, 0, ], ]

board = [[1],[0],[0],[1],[0],[0],[1],[0],[0],[1]]

board = [[1,1],[1,0]]

s = Solution()

z = np.array(s.gameOfLife(board))
