"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening_parens = '({['
        closing_parens = ')}]'
        stack = []
        for char in s:
            if char in opening_parens:
                stack.append(char)

            elif char in closing_parens and stack:
                if opening_parens.index(stack[-1]) != closing_parens.index(char):
                    return False
                stack.pop()
            else:
                return False
        return True if not stack else False

print(Solution().isValid("["))