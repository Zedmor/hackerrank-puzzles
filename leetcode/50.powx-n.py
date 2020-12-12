#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (29.30%)
# Total Accepted:    445.2K
# Total Submissions: 1.5M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
#
# Example 1:
#
#
# Input: 2.00000, 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: 2.10000, 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
# Note:
#
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
#
#
#
class Solution:
    """
    >>> Solution().myPow(8.84372, -5)
    1024.0

    >>> Solution().myPow(2.0000, 10)
    1024.0

    >>> Solution().myPow(2.10000, 3)
    9.26100

    >>> Solution().myPow(2.00000, -2)
    1024.00000

    >>> Solution().myPow(0.00001, 2147483647)
    1024.00000

    """
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        if n == 0:
            return 1

        result = x
        multiply_to = x
        while n > 1:
            if n % 2 != 0:
                result *= multiply_to
                multiply_to = x
                n -= 1
            else:
                n /= 2
                result *= multiply_to
                multiply_to = result

        return result


