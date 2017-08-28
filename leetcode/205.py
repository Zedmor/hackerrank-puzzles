"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sused = set()
        index = 0
        shash = dict.fromkeys(s,0)
        for letter in s:
            if letter not in sused:
                sused.add(letter)
                shash[letter] = index
                index +=1

        strans = []
        for letter in s:
            strans.append(shash[letter])


        thash = dict.fromkeys(t, 0)
        tused = set()
        index = 0
        for letter in t:
            if letter not in tused:
                tused.add(letter)
                thash[letter] = index
                index +=1

        ttrans = []
        for letter in t:
            ttrans.append(thash[letter])

        if ttrans == strans:
            return True
        else:
            return False

print(Solution().isIsomorphic('aba', 'baa'))