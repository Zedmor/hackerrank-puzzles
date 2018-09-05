"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
from collections import defaultdict

class Anagram(object):
    def __init__(self, anagram):
        self.anagram_representation = defaultdict(int)
        for char in anagram:
            self.anagram_representation[char] += 1
    def __repr__(self):
        return tuple(sorted(self.anagram_representation.items()))

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        all_anagrams = defaultdict(list)
        for anagram in strs:
            all_anagrams[Anagram(anagram).__repr__()].append(anagram)
        return list(all_anagrams.values())


input = ["hos", "boo", "nay", "deb", "wow", "bop", "bob", "brr", "hey", "rye", "eve", "elf", "pup", "bum", "iva", "lyx",
         "yap", "ugh", "hem", "rod", "aha", "nam", "gap", "yea", "doc", "pen", "job", "dis", "max", "oho", "jed", "lye",
         "ram", "pup", "qua", "ugh", "mir", "nap", "deb", "hog", "let", "gym", "bye", "lon", "aft", "eel", "sol", "jab"]

output = [["sol"], ["wow"], ["gap"], ["hem"], ["yap"], ["bum"], ["ugh", "ugh"], ["aha"], ["jab"], ["eve"], ["bop"],
          ["lyx"], ["jed"], ["iva"], ["rod"], ["boo"], ["brr"], ["hog"], ["nay"], ["mir"], ["deb", "deb"], ["aft"],
          ["dis"], ["yea"], ["hos"], ["rye"], ["hey"], ["doc"], ["bob"], ["eel"], ["pen"], ["job"], ["max"], ["oho"],
          ["lye"], ["ram"], ["nap"], ["elf"], ["qua"], ["pup", "pup"], ["let"], ["gym"], ["nam"], ["bye"], ["lon"]]


print(Solution().groupAnagrams(input))
