#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (42.92%)
# Total Accepted:    215.1K
# Total Submissions: 473.9K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
from collections import defaultdict
from typing import List

'[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'


#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# Example:
#
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Constraints:
#
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 0 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= i <= j < nums.length
#
#
#

def find_best_interval(intervals, j):
    # """
    # >>> find_best_interval([(1,3), (4,5)], 4)
    # (1, 3)
    #
    # :param intervals:
    # :param j:
    # :return:
    # """
    intervals.sort(key=lambda i: i[1])
    for interval in intervals[::-1]:
        if interval[1] <= j:
            return interval


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.precomputed_intervals = {}
        self.intervals_starts = defaultdict(list)
        self.intervals_ends = defaultdict(list)

    def sumRange(self, i: int, j: int) -> int:
        self.precomputed_intervals[(i, j)] = self.calculate_sum(i, j)
        self.intervals_starts[i].append((i, j))
        self.intervals_ends[j].append((i, j))
        return self.precomputed_intervals[(i, j)]

    def calculate_sum(self, i, j):
        accumulator = 0
        cursor = i
        while cursor <= j:
            if cursor in self.intervals_starts:
                best_interval = find_best_interval(self.intervals_starts[cursor], j)
                if best_interval:
                    accumulator += self.precomputed_intervals[best_interval]
                    cursor = best_interval[1] + 1

            else:
                accumulator += self.nums[cursor]
                self.precomputed_intervals[(i, cursor)] = accumulator
                self.intervals_starts[i].append((i, cursor))
                self.intervals_ends[cursor].append((i, cursor))
                cursor += 1
        return accumulator






# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
#
# obj = NumArray([-2, 0, 3, -5, 2, -1])
#
# assert obj.sumRange(0, 2) == 1
# assert obj.sumRange(2, 5) == -1
# assert obj.sumRange(0, 5) == -3

obj = NumArray([1, 4, -6])


assert obj.sumRange(0, 2) == -1
assert obj.sumRange(1, 2) == -2
assert obj.sumRange(0, 1) == 5

