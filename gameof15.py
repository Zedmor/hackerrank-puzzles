# python3.5

import heapq
import itertools
import numpy as np


class Board:
    def __init__(self, board):
        self.goalconfig = list(range(1, 16)) + [0]
        self.board = board
        self.distancefromstart = 0
        self.parent = None
        self.distance = self.calculate_distance()

    def __repr__(self):
        # TODO refactor this method
        return ('\nBoard: \n{} \nDistance: {}\nFrom start:{}'.
                format(np.matrix(self.board).reshape(4, 4),
                       self.getdistance(), self.distancefromstart))

    def __gt__(self, board2):
        return self.gettotaldistance() > board2.gettotaldistance()

    def __lt__(self, board2):
        return self.gettotaldistance() < board2.gettotaldistance()

    def calculate_distance(self):
        """
        :return: Sum of taxicab distances between board and goal
        """
        distance = 0
        for index, tile in enumerate(self.board):
            if tile is not self.goalconfig[index]:
                distance += self.taxicabdistance(index,
                                                 self.goalconfig.index(tile))

        return distance

    def getdistance(self):
        return self.distance

    def gettotaldistance(self):
        return self.distance + self.distancefromstart

    def taxicabdistance(self, index1, index2):
        y1, x1 = divmod(index1, 4)
        y2, x2 = divmod(index2, 4)
        return abs(x2 - x1) + abs(y2 - y1)

    def swapwithindex(self, index):
        """
        :swaps index and empty cell.
        :return: Board object
        """
        tempboard = self.board[:]
        index0 = tempboard.index(0)
        tempboard[index0], tempboard[index] = tempboard[index], tempboard[
            index0]
        return Board(tempboard)

    def allpositions(self):
        """
        :return: List of possible boards that could be generated from instance board
        """
        import random
        empty = self.board.index(0)
        movable = [index for index in range(16) if
                   self.taxicabdistance(empty, index) == 1]
        boards = []
        for move in movable:
            boards.append(self.swapwithindex(move))
        random.shuffle(boards)
        return boards


def solver(board):
    """
    :board: Board object
    :closed: processed nodes
    :distancesdict: hashtable of proc.nodes
    :return: List of boards leading to solution
    """

    def pushpositions(board, queue, closed, distancesdict):
        """
        pushes all position of the board to priority queue
        :param queue: priority queue list
        :param board: Board object
        """
        if board.getdistance() == 0:
            return board
        for childboard in board.allpositions():
            childboard.parent = board
            childboard.distancefromstart = board.distancefromstart + 1
            if childboard.getdistance() == 0:
                return childboard
            try:
                if distancesdict[
                    str(childboard.board)] > childboard.gettotaldistance():
                    heapq.heappush(queue, childboard)
                    distancesdict[
                        str(childboard.board)] = childboard.gettotaldistance()
            except KeyError:
                heapq.heappush(queue, childboard)
                distancesdict[
                    str(childboard.board)] = childboard.gettotaldistance()

    open = []
    closed = []
    distancesdict = {str(board.board): 0}
    result = None
    heapq.heappush(open, board)
    while open:
        top = heapq.heappop(open)
        result = pushpositions(top, open, closed, distancesdict)
        if result:
            # todo Refactor when result found
            return result
        distancesdict[str(top.board)] = top.gettotaldistance()
        closed.append(top)


# board = Board([12,2,3,4,0,6,7,8,9,10,11,1,13,14,15, 5])
board = Board([5, 1, 7, 3, 9, 2, 11, 4, 13, 6, 15, 8, 0, 10, 14, 12])
board = Board([5, 2, 4, 8, 10, 0, 3, 14, 13, 6, 11, 12, 1, 15, 9, 7])
board = Board([11, 4, 12, 2, 5, 10, 3, 15, 14, 1, 6, 7, 0, 9, 8, 13])
board = Board([1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 10, 12, 14, 11, 15, 0])

result = solver(board)

while True:
    print(result)
    if result.parent:
        result = result.parent
    else:
        break
