"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastsp = 0
        begin = None
        if s:
            while s and s[-1]==' ':
                s = s[:-1]
        for i, let in enumerate(s):
            if let ==' ':
                lastsp = i
                begin = i

        return len(s) - lastsp -1 if begin != None else len(s)


print(Solution().lengthOfLastWord(" a  fff world    "))