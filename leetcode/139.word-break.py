#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (40.92%)
# Total Accepted:    648.5K
# Total Submissions: 1.6M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    """
    >>> Solution().wordBreak(s = "aaaaaaa", wordDict = ["aaaa", "aaa"])
    True

    >>> Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"])
    True

    >>> Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
    True

     >>> Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
     False

    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        graph = {}
        for word in wordDict:
            cursor = graph
            for letter in word:
                cursor = cursor.setdefault(letter, {})
            cursor['$'] = '$'

        @lru_cache(None)
        def recur(s):
            if not s:
                return True
            cursor = graph
            for i, letter in enumerate(s):
                if letter not in cursor:
                    return False
                cursor = cursor[letter]
                if '$' in cursor:
                    result = recur(s[i + 1:])
                    if result:
                        return result
            return False

        return recur(s)







