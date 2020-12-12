#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.27%)
# Total Accepted:    84K
# Total Submissions: 345.7K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
# Example 2:
#
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
#
# Note:
#
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#
#
#
class Solution:
    """
    >>> Solution().checkSubarraySum([23, 2, 6, 4, 7], 0)
    False
    >>> Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
    True
    >>> Solution().checkSubarraySum([23, 2, 6, 4, 7], 6)
    True
    """
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        def check(n):
            try:
                if n % k == 0:
                    return True
            except ZeroDivisionError:
                if n == 0:
                    return True

        sums = {}
        current = 0

        l = 0
        current = nums[l]
        for r in range(l + 2, len(nums) + 1):
            current += nums[r - 1]
            sums[r] = current
            if check(current):
                return True

        # print(sums)
        # print('---')

        for l in range(len(nums) - 1):
            del sums[l + 2]
            # print(nums[l], sums)
            for r in range(l + 3, len(nums) + 1):
                sums[r] -= nums[l]
                if check(sums[r]):
                    return True

        return False






