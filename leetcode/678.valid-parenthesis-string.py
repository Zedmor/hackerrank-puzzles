#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (30.76%)
# Total Accepted:    108.5K
# Total Submissions: 351.9K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#
#
from copy import copy


class Solution:
    """
    >>> Solution().checkValidString('(*))')
    True

    >>> Solution().checkValidString('(*)')
    True

    >>> Solution().checkValidString('()')
    True

    >>> Solution().checkValidString('())')
    False

    >>> Solution().checkValidString('(()())')
    True

    >>> Solution().checkValidString('(()')
    False

    >>> Solution().checkValidString("(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)")
    True

    >>> Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
    False

    """
    def checkValidString(self, s: str) -> bool:
        stacks = set([tuple()])
        for char in s:
            if char == '*':
                new_stacks = set()
                for stack in copy(stacks):
                    if stack:
                        new_stack = stack - 1
                        new_stack.pop()
                        new_stacks.add(tuple(new_stack))
                    new_stack = list(copy(stack))
                    new_stack.append('(')
                    new_stacks.add(tuple(new_stack))
                stacks = stacks.union(new_stacks)
            if char in ('(', ')'):
                new_stacks = set()
                for stack in copy(stacks):
                    if char == ')':
                        if stack and stack[-1] == '(':
                            new_stack = list(stack)
                            stacks.remove(stack)
                            new_stack.pop()
                            new_stacks.add(tuple(new_stack))
                        else:
                            stacks.remove(stack)
                    else:
                        new_stack = list(stack)
                        new_stack.append(char)
                        new_stacks.add(tuple(new_stack))
                        stacks.remove(stack)
                stacks = stacks.union(new_stacks)

        return any([not stack for stack in stacks])



