#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/
#
# algorithms
# Hard (33.11%)
# Total Accepted:    9.7K
# Total Submissions: 29.3K
# Testcase Example:  '1'
#
# Given a positive integer n, find the number of non-negative integers less
# than or equal to n, whose binary representations do NOT contain consecutive
# ones.
#
# Example 1:
#
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers
#
#
# Note:
# 1
#
#
"""
>>> Solution().findIntegers(1000)
4181
"""
from math import log


class Solution:
    def findIntegers(self, num: int) -> int:

        FibArray = [0, 1]

        def fibonacci(n):
            if n < 0:
                print("Incorrect input")
            elif n <= len(FibArray):
                return FibArray[n - 1]
            else:
                temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
                FibArray.append(temp_fib)
                return temp_fib

        progression = 1
        counter = 0
        local_counter = 0
        for n in range(num + 1):
            # if n == 2 ** progression:
            #     print(local_counter)
            #     progression += 1
            #     local_counter = 0
            bin_rep = "{0:b}".format(n)
            if '11' not in bin_rep:
                counter += 1
                # local_counter += 1
            try:
                math_calc = int(log(n) / log(2)) + 4
                fib_calc = fibonacci(math_calc)
            except ValueError:
                fib_calc = 1
            print(f'N = {n}, naive: {counter}, fib: {fib_calc}')

        math_calc = int(log(num) / log(2)) + 4
        return fibonacci(math_calc)



