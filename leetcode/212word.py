# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]




class Board(object):
    def __init__(self, board):
        self.board = board

    def findword(self, word):
        def findwordfrompos(word, root, found=False, visited=[]):

            y, x = root
            if x >= 0 and x < maxX and y >= 0 and y < maxY and root not in visited:
                if board[y][x] == word[0]:
                    # print(board[root[0]][root[1]])
                    if len(word) == 1:
                        return True
                    found = findwordfrompos(word[1:], (y, x - 1), found,
                                            visited + [root])
                    found = findwordfrompos(word[1:], (y, x + 1), found,
                                            visited + [root])
                    found = findwordfrompos(word[1:], (y - 1, x), found,
                                            visited + [root])
                    found = findwordfrompos(word[1:], (y + 1, x), found,
                                            visited + [root])
            if found:
                return True

        board = self.board
        maxY = len(board)
        for i in range(maxY):

            if type(board[i]) == str:
                board[i] = list(board[i])

        maxX = len(board[0])
        visited = []
        # print('####{}########'.format(word))
        for x in range(maxX):
            for y in range(maxY):
                if board[y][x] == word[0]:
                    # visited.append((x,y))
                    root = (y, x)
                    if findwordfrompos(word, root):
                        return True
        return False


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        words = words

        board = board

        board = Board(board)

        # print(board.board)
        solution = []
        for word in words:
            if board.findword(word) and word not in solution:
                solution.append(word)
        return solution


a = Solution()
# print(a.findWords([
#              ['o', 'a', 'a', 'n'],
#              ['e', 't', 'a', 'e'],
#              ['i', 'h', 'k', 'r'],
#              ['i', 'f', 'l', 'v']
#          ],["oath", "pea", "eat", 'eat', "rain"] ))

print(a.findWords(['aa'], ['aaa']))
