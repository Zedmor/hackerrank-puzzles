"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

>>> Solution().merge([[1,19],[2,6],[8,10],[15,18]])
[[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

>>> Solution().merge([[1,4],[4,5]])
[[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:
    def merge(self, intervals):
        left_sorted = sorted(intervals)
        right_sorted = sorted(intervals, key=lambda i: i[1])
        print(left_sorted)

