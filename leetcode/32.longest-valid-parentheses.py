#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.67%)
# Total Accepted:    311.1K
# Total Submissions: 1.1M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
#
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
#
#
#
class Solution:
    """
    >>> Solution().longestValidParentheses('(()()')
    4

    >>> Solution().longestValidParentheses(')()())')
    4

    >>> Solution().longestValidParentheses('(()')
    2

    >>> Solution().longestValidParentheses('()(()')
    2

    >>> Solution().longestValidParentheses('')
    0

    """
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_counter = 0
        counter = 0
        counters = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    if not stack:
                        counter += 2
                    else:
                        counters.append(counter)
                        counter = 2

                elif not stack:
                    max_counter = max(max_counter, sum(counters), counter)
                    counter = 0
                    counters = []
        counters.append(counter)
        if stack:
            return max(max_counter, max(counters))
        return max(max_counter, sum(counters))
