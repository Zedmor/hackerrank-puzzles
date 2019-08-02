"""

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
>>> Solution().addBinary('1010', '1011')
10101


>>> Solution().addBinary('11', '1')
100



"""
from itertools import zip_longest


class Solution:
    def addBinary(self, a, b):
        carryover = 0
        result = []
        for pair in zip_longest(reversed(a), reversed(b), fillvalue=0):
            sum_digits = sum(map(int, pair)) + carryover
            if sum_digits == 2:
                carryover = 1
                sum_digits = 0
            elif sum_digits == 3:
                sum_digits = 1
                carryover = 1
            else:
                carryover = 0
            result = [sum_digits] + result
        if carryover == 1:
            result = [1] + result
        return ''.join(map(str, result))



        # if not digits:
        #     return digits
        # carryover = 0
        # digits[-1] += 1
        # for i in range(len(digits) - 1, -1, -1):
        #     digits[i] += carryover
        #     if digits[i] > 9:
        #         carryover = 1
        #         digits[i] = 0
        #     else:
        #         carryover = 0
        #
        # if carryover == 1:
        #     digits = [1] + digits
        #
        # return digits
        #
