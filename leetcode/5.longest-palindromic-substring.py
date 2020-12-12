#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.03%)
# Total Accepted:    896.5K
# Total Submissions: 3.1M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#
from collections import Counter
from copy import copy
from functools import lru_cache


@lru_cache(1024)
def is_palyndrome(left, right, s, lr):
    if left > right:
        return lr

    if s[left] != s[right]:
        return is_palyndrome(left + 1, right - 1, s, (left, right))

    return is_palyndrome(left + 1, right - 1, s, lr)

class Solution:
    """
    >>> Solution().longestPalindrome('bb')
    'bb'

    >>> Solution().longestPalindrome('abbcccbbbcaaccbababcbcabca')
    'bbcccbb'

    >>> Solution().longestPalindrome('ac')
    'a'

    >>> Solution().longestPalindrome('a')
    'a'

    >>> Solution().longestPalindrome('babad')
    'bab'

    >>> Solution().longestPalindrome('cbbd')
    'bb'

    """
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        left = 0
        right = len(s) - 1

        results = []


        @lru_cache(1024)
        def dfs(left, right):


            if left > right:
                return ''
            if is_palyndrome(left, right, s, (left, right)):
                return s[left: right + 1]
            v1 = dfs(left + 1, right)
            v2 = dfs(left, right - 1)
            if len(v1) > len(v2):
                return v1
            return v2
        return dfs(left, right)



