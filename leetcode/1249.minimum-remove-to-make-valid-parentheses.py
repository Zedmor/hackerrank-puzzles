#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (61.01%)
# Total Accepted:    75.5K
# Total Submissions: 120.8K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters. 
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
#
# Formally, a parentheses string is valid if and only if:
#
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
#
#
#
# Example 1:
#
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
#
# Example 2:
#
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
#
#
# Example 3:
#
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Example 4:
#
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.
#
#
from copy import copy
from functools import lru_cache


class Solution:
    """
    >>> Solution().minRemoveToMakeValid('lee(t(c)o)de)')
    'lee(t(c)o)de'

    >>> Solution().minRemoveToMakeValid('ab(c)d')
    'ab(c)d'

    >>> Solution().minRemoveToMakeValid('(a(b(c)d)')
    '(a(bc)d)'

    >>> Solution().minRemoveToMakeValid('))((')
    ''

    >>> Solution().minRemoveToMakeValid('")((((()v))(()((s(())"')
    '"vs(())"'

    """
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            if char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.append(i)
        to_remove = set(to_remove + stack)
        new_s = [v for i, v in enumerate(s) if i not in to_remove]
        return ''.join(new_s)

