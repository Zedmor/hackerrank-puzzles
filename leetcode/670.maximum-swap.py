#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (42.35%)
# Total Accepted:    80K
# Total Submissions: 180.5K
# Testcase Example:  '2736'
#
#
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
#
#
# Example 1:
#
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
#
# Example 2:
#
# Input: 9973
# Output: 9973
# Explanation: No swap.
#
#
#
#
# Note:
#
# The given number is in the range [0, 10^8]
#
#
#
class Solution:
    """
    >>> Solution().maximumSwap(2736)
    7236

    >>> Solution().maximumSwap(9973)
    9973

    """
    def maximumSwap(self, num: int) -> int:
        splitted = list(str(num))
        with_indexes = [(t[1], t[0]) for t in enumerate(splitted)]
        with_indexes = sorted(with_indexes, reverse=True)
        for i, e in enumerate(splitted):
            while with_indexes and with_indexes[0][1] < i:
                with_indexes.pop(0)
            for e2 in with_indexes:
                if e2[0] > e:
                    splitted[i], splitted[e2[1]] = splitted[e2[1]], splitted[i]
                    return int(''.join(splitted))

        return int(''.join(splitted))



