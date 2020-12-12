#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (54.85%)
# Total Accepted:    90.7K
# Total Submissions: 162.8K
# Testcase Example:  '[1,2,1]'
#
#
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
#
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
#
#
#
# Note:
# The length of given array won't exceed 10000.
#
#
import heapq
from collections import namedtuple
from functools import partial
from typing import List


class Solution:
    """
    >>> Solution().nextGreaterElements([5,4,3,2,1])
    [-1, 5, 5, 5, 5]

    >>> Solution().nextGreaterElements([3,4,5,6,2,3])
    [4, 5, 6, -1, 3, 4]

    >>> Solution().nextGreaterElements([1, 2, 1])
    [2, -1, 2]
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        Element = namedtuple('Element', ('val', 'position'))
        heap = []
        solution = [-1] * len(nums)
        for run in (0, 1):
            for position, val in enumerate(nums):
                while heap and heap[0].val < val:
                    top = heapq.heappop(heap)
                    solution[top.position] = val
                if run == 0:
                    heapq.heappush(heap, Element(val, position))
        return solution


