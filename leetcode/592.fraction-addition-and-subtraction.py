#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#
# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (48.25%)
# Total Accepted:    17.8K
# Total Submissions: 36.5K
# Testcase Example:  '"-1/2+1/2"'
#
# Given a string representing an expression of fraction addition and
# subtraction, you need to return the calculation result in string format. The
# final result should be irreducible fraction. If your final result is an
# integer, say 2, you need to change it to the format of fraction that has
# denominator 1. So in this case, 2 should be converted to 2/1.
#
# Example 1:
#
# Input:"-1/2+1/2"
# Output: "0/1"
#
#
#
# Example 2:
#
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
#
#
#
# Example 3:
#
# Input:"1/3-1/2"
# Output: "-1/6"
#
#
#
# Example 4:
#
# Input:"5/3+1/3"
# Output: "2/1"
#
#
#
# Note:
#
# The input string only contains '0' to '9', '/', '+' and '-'. So does the
# output.
# Each fraction (input and output) has format ±numerator/denominator. If the
# first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and
# denominator of each fraction will always be in the range [1,10]. If the
# denominator is 1, it means this fraction is actually an integer in a fraction
# format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid
# and in the range of 32-bit int.
#
#
#
import re
from math import gcd


class Fraction:
    def __init__(self, s):
        self.num, self.den = map(int, s.split('/'))

    def __repr__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        den = self.den
        new_num = self.num * other.den
        new_den = self.den * other.den
        new_other_num = other.num * den
        return Fraction(f'{new_num + new_other_num}/{new_den}')

    def __sub__(self, other):
        den = self.den
        new_num = self.num * other.den
        new_den = self.den * other.den
        new_other_num = other.num * den
        return Fraction(f'{new_num - new_other_num}/{new_den}')


class Solution:
    """
    >>> Solution().fractionAddition("-4/7-3/4+2/3")
    ''

    >>> Solution().fractionAddition("-5/2+10/3+7/9")
    '29/18'

    >>> Solution().fractionAddition("-1/2+1/2")
    '0/1'

    >>> Solution().fractionAddition("-1/2+1/2+1/3")
    '1/3'

    >>> Solution().fractionAddition("1/3-1/2")
    '-1/6'

    >>> Solution().fractionAddition("5/3+1/3")
    '2/1'

    """

    def fractionAddition(self, expression: str) -> str:
        groups = re.findall('-?[0-9]+\/[0-9]+', expression)
        operations = []
        expression = list(expression)
        for token in groups:
            if token.startswith('-') and operations:
                operations[-1] = '+'
            expression = expression[len(token):]
            if expression:
                operations.append(expression.pop(0))

        if groups:
            value = Fraction(groups.pop(0))

        while operations:
            op = operations.pop(0)
            if op == '+':
                value += Fraction(groups.pop(0))
            if op == '-':
                value -= Fraction(groups.pop(0))

        value.num, value.den = value.num // gcd(value.num, value.den), value.den // gcd(value.num, value.den)

        return f'{value.num}/{value.den}'
