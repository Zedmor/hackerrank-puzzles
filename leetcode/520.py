"""Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way."""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        hasupper = False
        haslower = False
        for letter in word[1:]:
            if 'Z' >= letter >= 'A':
                if  'z' >= word[0] >= 'a' or haslower:
                    return False
                hasupper = True
            elif 'z' >= letter >= 'a':

                if hasupper:
                    return False
                haslower = True


        return True


a = Solution()
print(a.detectCapitalUse("USA"))