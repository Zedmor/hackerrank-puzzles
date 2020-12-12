#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#
# https://leetcode.com/problems/word-subsets/description/
#
# algorithms
# Medium (46.98%)
# Total Accepted:    23K
# Total Submissions: 47.9K
# Testcase Example:  '["amazon","apple","facebook","google","leetcode"]\n["e","o"]'
#
# We are given two arrays A and B of words.  Each word is a string of lowercase
# letters.
#
# Now, say that word b is a subset of word a if every letter in b occurs in a,
# including multiplicity.  For example, "wrr" is a subset of "warrior", but is
# not a subset of "world".
#
# Now say a word a from A is universal if for every b in B, b is a subset of
# a.
#
# Return a list of all universal words in A.  You can return the words in any
# order.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
#
#
#
# Example 2:
#
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
#
#
#
# Example 3:
#
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
#
#
#
# Example 4:
#
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
#
#
#
# Example 5:
#
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B =
# ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
#
#
#
#
# Note:
#
#
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].
#
from collections import defaultdict, Counter
from copy import copy
from operator import itemgetter
from typing import List


class Solution:
    """
    >>> Solution().wordSubsets(A = ["bcedecccdb","daeeddecbc","ecceededdc","edadadccea","ebacdedcea","eddabdacec","cddbecbeca","eeababedcc","bcaddcdbad","aeeeeabeea"], B = ["cb","aae","ccc","ab","adc"])
    []

    >>> Solution().wordSubsets(A = ["abbac","ccbcc","abbbb","babca","accab"], B = ["c","c","c"])
    ["facebook", "google", "leetcode"]

    >>> Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"])
    ["facebook", "google", "leetcode"]

    >>> Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"])
    ["apple", "google", "leetcode"]

    >>> Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"])
    ["facebook", "google"]

    >>> Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"])
    ["google", "leetcode"]

    >>> Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"])
    ["facebook", "leetcode"]

    """
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        lookup = defaultdict(set)
        for word in A:
            counter = defaultdict(int)
            for letter in word:
                counter[letter] += 1
                lookup[(letter, counter[letter])].add(word)

        collector = set()
        for word in B:
            counts = Counter(word)
            collector = collector.union(set(counts.items()))

        sets = itemgetter(*collector)(lookup)
        if isinstance(sets, tuple):
            return list(set.intersection(*sets))
        return list(sets)
