#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# https://leetcode.com/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (40.57%)
# Total Accepted:    9.1K
# Total Submissions: 22.1K
# Testcase Example:  '"abc"'
#
# Given a string S, count the number of distinct, non-empty subsequences of S
# .
#
# Since the result may be large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
#
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
#
#
#
# Example 2:
#
#
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and
# "aba".
#
#
#
# Example 3:
#
#
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
#
#
#
#
#
#
#
#
# Note:
#
#
# S contains only lowercase letters.
# 1 <= S.length <= 2000
#
#
#
#
#
#
#
#
#
#


class Solution:
    """
    >>> Solution().distinctSubseqII('abcabc')
    7

    >>> Solution().distinctSubseqII('aba')
    6

    >>> Solution().distinctSubseqII('aaa')
    3
    """
    def distinctSubseqII(self, S: str) -> int:
        A = {k: 0 for k in set(S)}
        chars = set()
        B = 0

        for a in S:
            B_new = B + (B - A[a])
            A[a] = B
            B = B_new
            if a not in chars:
                chars.add(a)
                B += 1

        return B % (10 ** 9 + 7)

