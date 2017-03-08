
import copy
import random

class Solution(object):
    def checkintegrity(self, boardarray):
        for row in boardarray:
            assert set(row) == set(range(1, 10))
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def strtoarray(stringwithdots):
            """
            :param stringwithdots: string with . separates numbers
            :return: numpy array
            """
            stringwithdots = [int(char) if "." not in char else 0 for char in
                              stringwithdots]
            return stringwithdots

        def constructsetinterception():
            """
            :return: List of tuples with SQARE, ROW, COL of intersecting sets. With squares numbered 0-8.
            Let's say first intersection is (0,0,0)  - this means it's an intersection of SQ:0, COL:0 and ROW:0
            and all digits has to be different in each of this sets.
            """
            pass

        def belonging(row, col):
            """
            :param row:
            :param col:
            :return: tuple of (sqare, row, col)
            """
            return (
                row // 3 * 3 + col // 3,
                row,
                col
            )

        positions = []
        for i in range(9):
            for j in range(9):
                positions.append(belonging(i, j))

        def initialmatrix():
            for row in boardasarray:
                possibilities = set(range(0, 10)) - set(row)
                for i, position in enumerate(row):
                    if position == 0:
                        row[i] = possibilities

        def checkintegrity(coordinates):
            testlist = []
            for coord in coordinates:
                if type(boardasarray[coord[0]][coord[1]]) == int:
                    testlist.append(boardasarray[coord[0]][coord[1]])
            return len(testlist) == len(set(testlist))

        def optimizesequence(coordinates):
            """
            :param coordinates: list of coordinates to be optimized in format (row, col)
            :return: optimized list of coordinates
            """
            findsingularsets(coordinates)
            sqset = set()
            for coord in coordinates:
                if type(boardasarray[coord[0]][coord[1]]) == int:
                    sqset.add(boardasarray[coord[0]][coord[1]])
            possibilities = set(range(1, 10)) - sqset
            for coord in coordinates:
                if type(boardasarray[coord[0]][coord[1]]) == set:
                    boardasarray[coord[0]][coord[1]] = set.intersection(
                        possibilities,
                        boardasarray[coord[0]][coord[1]])

                allvalues = []

                for coord in coordinates:
                    if type(boardasarray[coord[0]][coord[1]]) == set:
                        allvalues += list(boardasarray[coord[0]][coord[1]])
                uniquevals = set(
                    [x for x in allvalues if
                     allvalues.count(x) == 1]) - possibilities
                if uniquevals:
                    for coord in coordinates:

                        if type(boardasarray[coord[0]][
                                    coord[1]]) == set and set.intersection(
                            uniquevals,
                            boardasarray[coord[0]][coord[1]]) != set():
                            replacement = set.intersection(
                                uniquevals,
                                boardasarray[coord[0]][coord[1]]).pop()
                            uniquevals.remove(replacement)
                            # boardasarray[coord[0]][coord[1]] =

                if not checkintegrity(coordinates):
                    integritycheck = False

        def optimizerows():
            for row in range(9):
                coords = [(row, n) for n in range(9)]
                optimizesequence(coords)

        def optimizecols():
            for col in range(9):
                coords = [(n, col) for n in range(9)]
                optimizesequence(coords)

        def optimizesquares():
            for square in range(9):
                currentsqcoords = [(coord[1], coord[2]) for coord in positions
                                   if coord[0] == square]
                optimizesequence(currentsqcoords)


        def findsingularsets(coordinates):
            for coord in coordinates:
                if type(boardasarray[coord[0]][coord[1]]) is set and len(
                        boardasarray[coord[0]][coord[1]]) == 1:
                    boardasarray[coord[0]][coord[1]] = int(
                        boardasarray[coord[0]][coord[1]].pop())

        def isboardconveges(brdarray):
            for row in brdarray:
                if any(isinstance(x, set) for x in row):
                    return False
            else:
                return True

        def sudokuintcheck(boardasarray):
            import itertools
            def grouper(iterable, n):
                it = iter(iterable)
                while True:
                    chunk = tuple(itertools.islice(it, n))
                    if not chunk:
                        return
                    yield chunk

            coords = []
            for row in range(9):
                coords += [(row, n) for n in range(9)]
                coords += [(n, row) for n in range(9)]
                coords += [(coord[1], coord[2]) for coord in positions
                           if coord[0] == row]
            for each in grouper(coords, 9):
                testset = []
                for eachone in each:
                    testset.append(boardasarray[eachone[0]][eachone[1]])
                if set(testset) != set(range(1, 10)):
                    return False
            return True

        boardasarray = [strtoarray(boardrow) for boardrow in board]
        boardbeforetransformation = copy.deepcopy(boardasarray)
        initialmatrix()
        # findsingularsets()

        while boardbeforetransformation != boardasarray:
            boardbeforetransformation = copy.deepcopy(boardasarray)
            optimizerows()
            optimizecols()
            optimizesquares()

        setcoords = []
        for i in range(9):
            for j in range(9):
                if type(boardasarray[i][j]) is set:
                    setcoords.append((i, j))


        integritycheck = True
        backupboard = copy.deepcopy(boardasarray)

        while not isboardconveges(boardasarray) or not integritycheck:
            expercoord = random.choice(setcoords)
            if boardasarray[expercoord[0]][expercoord[1]]:
                boardasarray[expercoord[0]][expercoord[1]] = random.choice(list(
                    boardasarray[expercoord[0]][expercoord[1]]
                ))
            integritycheck = True
            boardbeforetransformation = copy.deepcopy(boardasarray)
            while True:
                boardbeforetransformation = copy.deepcopy(boardasarray)
                optimizerows()
                optimizecols()
                optimizesquares()
                if boardbeforetransformation == boardasarray or not integritycheck:
                    break
            if isboardconveges(
                    boardasarray) and integritycheck and sudokuintcheck(
                    boardasarray):
                break
            boardasarray = copy.deepcopy(backupboard)

        for i, row in enumerate(board):
            board[i] = ''.join(map(str, boardasarray[i]))
