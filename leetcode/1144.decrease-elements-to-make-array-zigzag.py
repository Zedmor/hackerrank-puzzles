#
# @lc app=leetcode id=1144 lang=python3
#
# [1144] Decrease Elements To Make Array Zigzag
#
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/description/
#
# algorithms
# Medium (44.92%)
# Total Accepted:    8.1K
# Total Submissions: 17.9K
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of integers, a move consists of choosing any element and
# decreasing it by 1.
#
# An array A is a zigzag array if either:
#
#
# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1]
# < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] <
# A[1] > A[2] < A[3] > A[4] < ...
#
#
# Return the minimum number of moves to transform the given array nums into a
# zigzag array.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation: We can decrease 2 to 0 or 3 to 1.
#
#
# Example 2:
#
#
# Input: nums = [9,6,1,6,2]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
#
#
#
from copy import copy
from typing import List


class Solution:
    """
    >>> Solution().movesToMakeZigzag([151,42,769,349,835,92,242,82,357,494,880,683,470,631,479,298,941,113,892,103,755,575,885,50,479,502,181,164,292,832,657,512,528,588,716,965,195,106,396,649])
    2463

    >>> Solution().movesToMakeZigzag([10,4,4,10,10,6,2,3])
    13

    >>> Solution().movesToMakeZigzag([1,2,3])
    2

    >>> Solution().movesToMakeZigzag([9,6,1,6,2])
    4
    """

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def min_neighbour(i, num):
            if i == 0:
                return num[i + 1]
            elif i == len(num) - 1:
                return num[i - 1]
            else:
                return min(num[i - 1], num[i + 1])

        costs = []
        for run in (0, 1):
            _num = copy(nums)
            cost = 0
            for i in range(run, len(_num), 2):
                if _num[i] >= min_neighbour(i, _num):
                    swap_cost = abs(_num[i] - min_neighbour(i, _num)) + 1
                    cost += swap_cost
                    _num[i] -= swap_cost
            costs.append(cost)
        return min(costs)
