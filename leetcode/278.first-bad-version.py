#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (31.47%)
# Total Accepted:    319.9K
# Total Submissions: 948.8K
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
#
# Example:
#
#
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version. 
#
#
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 1

class Solution:
    """
    >>> Solution().firstBadVersion(2)
    1

    >>> Solution().firstBadVersion(10)
    4
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0 if isBadVersion(0) else None

        left_bound = -1
        right_bound = n + 1
        guess = (right_bound + left_bound) // 2
        while not(isBadVersion(guess + 1) and not isBadVersion(guess)):
            if isBadVersion(guess):
                right_bound = guess + 1
            else:
                left_bound = guess - 1
            guess = left_bound + (right_bound - left_bound) // 2
        return guess + 1



