#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (47.97%)
# Total Accepted:    233.6K
# Total Submissions: 474.3K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given a string s and a string t, check if s is subsequence of t.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.
#
#
#
class Solution:
    """
    >>> Solution().isSubsequence('abc', 'ahbgdc')
    True

    >>> Solution().isSubsequence('axc', 'ahbgdc')
    False

    """
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0
        while pointer_t < len(t) and pointer_s < len(s):
            if t[pointer_t] == s[pointer_s]:
                pointer_s += 1

            pointer_t += 1
        return pointer_s == len(s)






