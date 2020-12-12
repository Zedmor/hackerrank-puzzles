#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#
# https://leetcode.com/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (54.11%)
# Total Accepted:    21.8K
# Total Submissions: 39.6K
# Testcase Example:  '"BCD"\n["BCG","CDE","GEA","FFF"]'
#
# We are stacking blocks to form a pyramid. Each block has a color which is a
# one letter string.
#
# We are allowed to place any color block C on top of two adjacent blocks of
# colors A and B, if and only if ABC is an allowed triple.
#
# We start with a bottom row of bottom, represented as a single string. We also
# start with a list of allowed triples allowed. Each allowed triple is
# represented as a string of length 3.
#
# Return true if we can build the pyramid all the way to the top, otherwise
# false.
#
# Example 1:
#
#
# Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
#     A
#    / \
#   G   E
#  / \ / \
# B   C   D
#
# We are allowed to place G on top of B and C because BCG is an allowed
# triple.  Similarly, we can place E on top of C and D, then A on top of G and
# E.
#
#
#
# Example 2:
#
#
# Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C !=
# D.
#
#
#
# Constraints:
#
#
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
# 'F', 'G'}.
#
#
#
from collections import defaultdict
from functools import lru_cache
from typing import List


def is_correct(pyr, row, col, letter, allowed):
    tmp = pyr[row][col]
    pyr[row][col] = letter
    for first_row, second_row in zip(pyr, pyr[1:]):
        for i in range(len(first_row)):
            triplet = tuple(second_row[i:i + 2] + [first_row[i]])
            if 0 in triplet:
                continue
            if triplet not in allowed:
                pyr[row][col] = tmp
                return False

    pyr[row][col] = tmp
    return True


def pyr_full(pyr):
    if pyr[0][0] != 0:
        return True
    return False


class Solution:
    """
    >>> Solution().pyramidTransition('AABA', ["AAA","AAB","ABA","ABB","BAC"])
    False

    >>> Solution().pyramidTransition('BCD', ["BCG", "CDE", "GEA", "FFF"])
    True

    >>> Solution().pyramidTransition('AABA', ["AAA", "AAB", "ABA", "ABB", "BAC"])
    False
    """
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        prefix_map = defaultdict(set)
        for triplet in allowed:
            prefix_map[tuple(triplet[:2])].add(triplet[2])

        allowed = {tuple(i) for i in allowed}
        board = [[0] * n for n in range(1, len(bottom))]
        board.append(list(bottom))

        def recur(board):
            if pyr_full(board):
                return True

            for row in range(len(board) - 2, -1, -1):
                for position in range(len(board[row])):
                    if board[row][position] == 0:
                        prefix = tuple(board[row + 1][position: position + 2])
                        if not prefix_map[prefix]:
                            return False
                        for letter in prefix_map[prefix]:
                            if is_correct(board, row, position, letter, allowed):
                                board[row][position] = letter
                                if recur(board) is True:
                                    return True
                                board[row][position] = 0
            return False

        return recur(board)
