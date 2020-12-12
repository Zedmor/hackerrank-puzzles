#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#
# https://leetcode.com/problems/decode-ways-ii/description/
#
# algorithms
# Hard (26.12%)
# Total Accepted:    33K
# Total Submissions: 123.2K
# Testcase Example:  '"*"'
#
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping way:
#
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#
# Beyond that, now the encoded string can also contain the character '*', which
# can be treated as one of the numbers from 1 to 9.
#
#
#
#
# Given the encoded message containing digits and the character '*', return the
# total number of ways to decode it.
#
#
#
# Also, since the answer may be very large, you should return the output mod
# 10^9 + 7.
#
#
# Example 1:
#
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C",
# "D", "E", "F", "G", "H", "I".
#
#
#
# Example 2:
#
# Input: "1*"
# Output: 9 + 9 = 18
#
#
#
# Note:
#
# The length of the input string will fit in range [1, 10^5].
# The input string will only contain the character '*' and digits '0' - '9'.
#
#
#
from itertools import zip_longest


def evaluate_pair(pair):
    """
    >>> evaluate_pair('00')
    0

    >>> evaluate_pair('19')
    2

    >>> evaluate_pair('92')
    1

    :param pair:
    :return:
    """
    total_combos = 0

    # if pair == ('*', None):
    #     return 0

    if '*' not in pair:

        if int(pair[0]) > 0:
            total_combos += 1

        if pair[1] is not None:
            if 10 <= int(''.join(pair)) <= 26:
                total_combos += 1

    elif '*' == pair[0]:
        for i in range(1, 10):
            total_combos += evaluate_pair((str(i), pair[1]))

    elif '*' == pair[1]:
        for i in range(1, 10):
            total_combos += evaluate_pair((pair[0], str(i)))

    return total_combos



class Solution:
    """
    >>> Solution().numDecodings('***')
    999

    >>> Solution().numDecodings('**')
    96

    >>> Solution().numDecodings('1925')
    4

    >>> Solution().numDecodings('*')
    9

    >>> Solution().numDecodings('1*')
    18
    """
    def numDecodings(self, s: str) -> int:
        if s == '*':
            return 9

        number_of_variants = 0
        variants = []
        for pair in zip_longest(s, s[1:]):
            variants.append(evaluate_pair(pair))
            v = evaluate_pair(pair)
            if v > 1:
                number_of_variants += v
        return variants
