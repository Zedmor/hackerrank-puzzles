#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (21.04%)
# Total Accepted:    119.8K
# Total Submissions: 564.2K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
#
# Example 1:
#
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
#
# Example 2:
#
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#
#
#
class Solution:
    """
    >>> Solution().fractionToDecimal(1, 2)
    '0.5'

    >>> Solution().fractionToDecimal(2, 1)
    '2'

    >>> Solution().fractionToDecimal(2, 3)
    '0.(6)'

    """
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:


