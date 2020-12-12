#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (42.94%)
# Total Accepted:    260.9K
# Total Submissions: 585.6K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#
from typing import List


class Solution:
    """
    >>> Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    11

    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sums = triangle[-1]
        cursor = len(triangle) - 2
        while cursor >= 0:
            sums = [min(sums[i] + n, sums[i+1] + n) for i, n in enumerate(triangle[cursor])]
            cursor -= 1
        return sums[0]

