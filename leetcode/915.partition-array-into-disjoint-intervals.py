#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (44.73%)
# Total Accepted:    20.2K
# Total Submissions: 44.5K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an array A, partition it into two (contiguous) subarrays left and right
# so that:
#
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
#
#
# Return the length of left after such a partitioning.  It is guaranteed that
# such a partitioning exists.
#
#
#
# Example 1:
#
#
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
#
#
#
# Note:
#
#
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.
#
#
#
#
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().partitionDisjoint([1,1])
    1

    >>> Solution().partitionDisjoint([5,0,3,8,6])
    3

    >>> Solution().partitionDisjoint([1,1,1,0,6,12])
    4

    """
    def partitionDisjoint(self, A: List[int]) -> int:
         cursor = 1
         left_max = max(A[:cursor])
         right_min = min(A[cursor:])
         while left_max > right_min:
             cursor += 1
             left_max = max(left_max, A[cursor - 1])
             right_min = min(A[cursor:])
         return cursor

