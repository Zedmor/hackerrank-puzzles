#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.52%)
# Total Accepted:    162K
# Total Submissions: 409.9K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
#
# Example 1:
#
#
# Input: [5,7]
# Output: 4
#
#
# Example 2:
#
#
# Input: [0,1]
# Output: 0
#
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        answer = 0
        for i in range(30, -1, -1):
            if m & (1 << i) != n & (1 << i):
                break
            answer |= (m & (1 << i))
        return answer


