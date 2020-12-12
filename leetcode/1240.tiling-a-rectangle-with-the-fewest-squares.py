#
# @lc app=leetcode id=1240 lang=python3
#
# [1240] Tiling a Rectangle with the Fewest Squares
#
# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/description/
#
# algorithms
# Hard (49.68%)
# Total Accepted:    7.5K
# Total Submissions: 14.9K
# Testcase Example:  '2\n3'
#
# Given a rectangle of size  n  x m, find the minimum number of integer-sided
# squares that tile the rectangle.
#
#
# Example 1:
#
#
#
#
# Input: n = 2, m = 3
# Output: 3
# Explanation: 3 squares are necessary to cover the rectangle.
# 2 (squares of 1x1)
# 1 (square of 2x2)
#
# Example 2:
#
#
#
#
# Input: n = 5, m = 8
# Output: 5
#
#
# Example 3:
#
#
#
#
# Input: n = 11, m = 13
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= n <= 13
# 1 <= m  <=  13
#
#
#
class Solution:
    """
    >>> Solution().tilingRectangle(2, 3)
    3

    >>> Solution().tilingRectangle(5, 8)
    5

    >>> Solution().tilingRectangle(11, 13)
    6
    """
    def tilingRectangle(self, n: int, m: int) -> int:
        counter = 0
        short_side = min(n, m)
        long_side = max(n, m)
        while short_side > 1:
            counter += long_side // short_side
            short_side, long_side = long_side % short_side, short_side
        return counter + long_side

