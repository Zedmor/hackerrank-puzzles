"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftnode = None
        self.rightnode = None


class Board(object):
    def __init__(self, position):
        self.board = position
        #self.clearboard()

    def __str__(self):
        return self.getPosition()

    def getPosition(self):
        return self.board

    def clearboard(self):
        i = 0
        while len(self.board) > 2 and i < len(self.board) - 2:
            while len(set(self.board[i:i + 3])) == 1 and len(
                    self.board[i:i + 3]) == 3:
                self.board = self.board[:i] + self.board[i + 3:]
                i = max(-1, i - 4)
            i += 1

    def insertMarble(self, marble, index):
        assert index < len(self.board) + 1
        self.board = self.board[:index] + marble + self.board[index:]
        self.clearboard()
        return self

    def pairIndices(self, marble):
        result = []
        for i in range(len(self.board)-1):
            if self.board[i] == self.board[i+1] == marble:
                result.append(i)
        return result

    def singleIndices(self, marble):
        result = []
        for i in range(len(self.board)):
            if self.board[i] == marble:
                result.append(i)
        return result

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def findsolution(original, hand, depth=0):
            options = []
            for marble in list(set(hand)):
                positions = original.pairIndices(marble)
                for position in positions:
                    copyboard = Board(original.board)
                    copyboard.insertMarble(marble, position)
                    options.append((marble, position, len(copyboard.board)))
            if not options: #Look for 1 of marble
                for marble in list(set(hand)):
                    positions = original.singleIndices(marble)
                    for position in positions:
                        copyboard = Board(original.board)
                        copyboard.insertMarble(marble, position)
                        options.append((marble, position, len(copyboard.board)))
            if not options:
                options = [(marble, 0, len(original.board)) for marble in list(set(hand))]
            # if options:
                #
            if len(options) > 1:
                # newoptions = []
                # for option in options:
                #     depth = findsolution(Board(original.board))
                #     depth.inse

                options = [(option[0], option[1], findsolution(Board(original.board).insertMarble(option[0],option[1]), [elofhand for elofhand in hand if elofhand != option[0]], depth+1))  for option in options]

                return options[0][2]
                # print(options)
            else:
                options = sorted(options, key=lambda x: x[2])
                bestoption = (options[0][0], options[0][1])
                bestoption = options[0]
                hand.remove(bestoption[0])
                original.insertMarble(*bestoption[:2])
                solution.append(bestoption)
                if len(original.board) == 0:
                    return depth
                if len(hand) ==0:
                    return float('inf')
                depth+=1
                return findsolution(Board(original.board), list(hand), depth+1)

        hand = list(hand)
        #original = Board(board)
        solution = []
        # while hand:
        sol = findsolution(Board(board), hand)
        if sol == float('inf'):
            return -1
        else:
            return sol
        # return -1




