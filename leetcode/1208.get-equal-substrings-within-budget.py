#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
#
# algorithms
# Medium (39.52%)
# Total Accepted:    16.9K
# Total Submissions: 39.7K
# Testcase Example:  '"abcd"\n"bcdf"\n3'
#
# You are given two strings s and t of the same length. You want to change s to
# t. Changing the i-th character of s to i-th character of t costs |s[i] -
# t[i]| that is, the absolute difference between the ASCII values of the
# characters.
#
# You are also given an integer maxCost.
#
# Return the maximum length of a substring of s that can be changed to be the
# same as the corresponding substring of twith a cost less than or equal to
# maxCost.
#
# If there is no substring from s that can be changed to its corresponding
# substring from t, return 0.
#
#
# Example 1:
#
#
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum
# length is 3.
#
# Example 2:
#
#
# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to charactor in t, so the
# maximum length is 1.
#
#
# Example 3:
#
#
# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You can't make any change, so the maximum length is 1.
#
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 10^5
# 0 <= maxCost <= 10^6
# s and t only contain lower case English letters.
#
#
#
class Solution:
    """
    >>> Solution().equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14)
    4

    >>> Solution().equalSubstring("krrgw", "zjxss", 19)
    2

    >>> Solution().equalSubstring("thjdoffka", "qhrnlntls", 11)
    3

    >>> Solution().equalSubstring('abcd', 'bcdf', 3)
    3

    >>> Solution().equalSubstring('abcd', 'cdef', 3)
    1

    >>> Solution().equalSubstring('abcd', 'acde', 0)
    1

    >>> Solution().equalSubstring('abcd', 'cdef', 1)
    0
    """

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = [abs(ord(t[0]) - ord(t[1])) for t in zip(s, t)]
        if not diffs:
            return 0
        left_pointer = 0
        right_pointer = 0
        total_cost = diffs[left_pointer]
        max_len = 0
        while right_pointer < len(diffs) - 1:
            while total_cost <= maxCost and right_pointer < len(diffs) - 1:
                right_pointer += 1
                total_cost += diffs[right_pointer]
            max_len = max(max_len, right_pointer - left_pointer)
            if right_pointer == len(diffs) - 1 and total_cost <= maxCost:
                max_len = max(max_len, right_pointer - left_pointer + 1)
            while total_cost > maxCost and left_pointer < right_pointer:
                total_cost -= diffs[left_pointer]
                left_pointer += 1
            if total_cost > maxCost and left_pointer == right_pointer and left_pointer < len(diffs) - 1:
                left_pointer += 1
                right_pointer += 1
                total_cost = diffs[left_pointer]

        return max_len
