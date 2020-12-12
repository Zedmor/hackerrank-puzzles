#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.98%)
# Total Accepted:    433.5K
# Total Submissions: 1.7M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#
#


class Solution:
    """
    # >>> Solution().numDecodings('***')
    # 999
    #
    # >>> Solution().numDecodings('**')
    # 96
    # >>> Solution().numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253")
    # 3981312

    # >>> Solution().numDecodings('101')
    # 1
    #
    # >>> Solution().numDecodings('100')
    # 0
    #
    # >>> Solution().numDecodings('01')
    # 0
    #
    # >>> Solution().numDecodings('10')
    # 1
    #
    # >>> Solution().numDecodings('0')
    # 0

    >>> Solution().numDecodings('226')
    3

    >>> Solution().numDecodings('1925')
    4

    # >>> Solution().numDecodings('*')
    # 9
    #
    # >>> Solution().numDecodings('1*')
    # 18
    """

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n < 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1  # an empty string will have one way to decode
        dp[1] = 0 if (s[0] == "0") else 1
        for i in range(2, n + 1):
            if 1 <= int(s[i - 1: i]) <= 10:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
