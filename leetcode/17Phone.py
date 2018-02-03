"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mappings = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        num_to_chars = [mappings[c] for c in digits]
        result = self.letterCombinations_from_chars(num_to_chars)
        return result if result!=[''] else []

    def letterCombinations_from_chars(self, num_to_chars):
        result = []
        if not num_to_chars:
            return ['']
        for letter in num_to_chars[0]:
            suffix = self.letterCombinations_from_chars(num_to_chars[1:])
            for s_letter in suffix:
                result.append(letter+s_letter)

        return result

print(Solution().letterCombinations(''))

