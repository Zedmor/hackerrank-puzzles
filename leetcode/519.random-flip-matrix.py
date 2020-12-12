#
# @lc app=leetcode id=519 lang=python3
#
# [519] Random Flip Matrix
#
# https://leetcode.com/problems/random-flip-matrix/description/
#
# algorithms
# Medium (35.88%)
# Total Accepted:    7.6K
# Total Submissions: 21.1K
# Testcase Example:  '["Solution", "flip", "flip", "flip", "flip"]\n[[2, 2], [], [], [], []]'
#
# You are given the number of rows n_rows and number of columns n_cols of a 2D
# binary matrix where all values are initially 0. Write a function flip which
# chooses a 0 value uniformly at random, changes it to 1, and then returns the
# position [row.id, col.id] of that value. Also, write a function reset which
# sets all values back to 0. Try to minimize the number of calls to system's
# Math.random() and optimize the time and space complexity.
#
# Note:
#
#
# 1 <= n_rows, n_cols <= 10000
# 0 <= row.id < n_rows and 0 <= col.id < n_cols
# flip will not be called when the matrix has no 0 values left.
# the total number of calls to flip and reset will not exceed 1000.
#
#
# Example 1:
#
#
# Input:
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
#
#
#
# Example 2:
#
#
# Input:
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]]
#
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, n_rows and n_cols. flip and reset
# have no arguments. Arguments are always wrapped with a list, even if there
# aren't any.
#
#
import random
from copy import copy
from typing import List


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.top_index = n_rows * n_cols - 1
        self.swaps = {}
        self.z = [1,2,0,0]

    def flip(self) -> List[int]:
        def norm(i):
            return [i // self.n_cols, i % self.n_cols]

        el = random.randint(0, self.top_index) if self.top_index > 0 else 0
        # el = self.z.pop(0)

        if el == self.top_index:
            self.top_index -= 1
            while el in self.swaps:
                el = self.swaps[el]
            return norm(el)
        if el in self.swaps:
            result = self.swaps[el]
            while result in self.swaps:
                result = self.swaps[result]
            self.swaps[el] = self.top_index
            self.top_index -= 1
            return norm(result)
        self.swaps[el] = self.top_index
        self.top_index -= 1
        return norm(el)

    def reset(self) -> None:
        self.top_index = self.n_rows * self.n_cols - 1
        self.swaps = {}


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

# obj = Solution(2,2)
# for i in range(4):
#     print(obj.flip())
# print()
# obj.reset()
# for i in range(4):
#     print(obj.flip())
