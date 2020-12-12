#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (29.91%)
# Total Accepted:    311K
# Total Submissions: 1M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
#

class Solution:
    """
    >>> Solution().countPrimes(10)
    4
    """
    def countPrimes(self, n: int) -> int:
        primes = [True for i in range(n + 1)]
        p = 2
        while p ** 2 <= n:
            if primes[p]:
                for i in range(p ** 2, n + 1, p):
                    primes[i] = False
            p += 1
        return sum(primes[2:])
