"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

Subscribe to see which companies asked this question.
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = 'AaEeIiOoUu'
        vwinx = []
        for i, char in enumerate(s):
            if char in vowels:
                vwinx.append(i)
        for vpos in range(len(vwinx)//2):
            s[vwinx[vpos]] , s[vwinx[len(vwinx)-vpos-1]] = s[vwinx[len(vwinx)-vpos-1]], s[vwinx[vpos]]
        return ''.join(s)

print(Solution().reverseVowels("leetcode"))