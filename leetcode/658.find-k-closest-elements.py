#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (40.00%)
# Total Accepted:    119.9K
# Total Submissions: 290.8K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted array arr, two integers k and x, find the k closest elements
# to x in the array. The result should also be sorted in ascending order. If
# there is a tie, the smaller elements are always preferred.
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# Absolute value of elements in the array and x will not exceed 10^4
#
#
#
from bisect import bisect_left
from typing import List


class Solution:
    """
    >>> Solution().findClosestElements([1,1,1,10,10,10], k = 1, x = 9)
    [10]

    >>> Solution().findClosestElements([1,2,3,4,5], k = 4, x = -1)
    [1, 2, 3, 4]

    >>> Solution().findClosestElements([1], k = 1, x = 1)
    [1]

    >>> Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], k = 3, x = 5)
    [3, 3, 4]

    >>> Solution().findClosestElements([1,2,3,4,5], k = 4, x = 3)
    [1, 2, 3, 4]
    """

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect_left(arr, x)
        if pos == 0:
            best_point = 0
        elif pos == len(arr):
            best_point = len(arr) - 1

        else:
            before = arr[pos - 1]
            after = arr[pos]
            if after - x < x - before:
                best_point = pos
            else:
                best_point = pos - 1

        left_pointer = best_point
        right_pointer = best_point

        while right_pointer - left_pointer < k - 1:

            if left_pointer > 0 and right_pointer < len(arr) - 1:
                if abs(arr[left_pointer - 1] - x) <= abs(arr[right_pointer + 1] - x):
                    left_pointer -= 1
                    continue
                else:
                    right_pointer += 1
                    continue
            if left_pointer > 0:
                left_pointer -= 1
                continue
            if right_pointer < len(arr) - 1:
                right_pointer += 1

        return arr[left_pointer: right_pointer + 1]
