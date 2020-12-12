#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (40.98%)
# Total Accepted:    175.2K
# Total Submissions: 426.9K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
#
#
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
#
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
#
# Example 3:
#
#
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.
#
#
# Note:
#
#
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
#
#
import math


class Solution:
    def isUgly(self, num: int) -> bool:

        if num == 1:
            return True

        if num == 0:
            return False

        primes = set()

        # Print the number of two's that divide n
        while num % 2 == 0:
            primes.add(2)
            num = num / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        r = range(3, int(math.sqrt(num)) + 1, 2) if num > 0 else range(-3, -int(math.sqrt(abs(num))) - 1, -2)
        for i in r:

            # while i divides n , print i ad divide n
            while num % i == 0:
                primes.add(int(i))
                num = num / i

                # Condition if n is a prime
        # number greater than 2
        if num > 2 or num < -2:
            primes.add(int(num))

        if num == -1:
            return False

        return len(primes) > 0 and primes.issubset({2, 3, 5})


# print(Solution().isUgly(6))
print(Solution().isUgly(-6))
