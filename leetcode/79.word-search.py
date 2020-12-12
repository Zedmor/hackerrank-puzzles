#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (34.16%)
# Total Accepted:    548.1K
# Total Submissions: 1.5M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where "adjacent" cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# board  and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
    True

    >>> Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
    True

    >>> Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
    False

    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        start_coords = [(row, col)
                        for row in range(len(board))
                        for col in range(len(board[0]))
                        if board[row][col] == word[0]]

        def recur(coord, word, path=None):
            if not word:
                return True
            if not path:
                path = []
            if coord[0] - 1 >= 0 and board[coord[0] - 1][coord[1]] == word[0] and (coord[0] - 1, coord[1]) not in path:
                if recur((coord[0] - 1, coord[1]), word[1:], path + [coord]):
                    return True
            if coord[0] + 1 < len(board) and board[coord[0] + 1][coord[1]] == word[0] and (coord[0] + 1, coord[1]) not in \
                    path:
                if recur((coord[0] + 1, coord[1]), word[1:], path + [coord]):
                    return True
            if coord[1] - 1 >= 0 and board[coord[0]][coord[1] - 1] == word[0] and (coord[0], coord[1] - 1) not in path:
                if recur((coord[0], coord[1] - 1), word[1:], path + [coord]):
                    return True
            if coord[1] + 1 < len(board[0]) and board[coord[0]][coord[1] + 1] == word[0] and (coord[0],
                                                                                           coord[1] + 1) not in \
                    path:
                if recur((coord[0], coord[1] + 1), word[1:], path + [coord]):
                    return True

        return any(recur(coord, word[1:]) for coord in start_coords)


