"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



>>> Solution().insert([], [5,7])
[[5, 7]]


Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
>>> Solution().insert([[1,3],[6,9]], [2,5])
[[1, 5], [6, 9]]

Example 2:

>>> Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
[[1, 2], [3, 10], [12, 16]]

Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        all_intervals = set([tuple(i) for i in intervals])
        right_sorted = iter(sorted(intervals, key=lambda i: (i[1], i[0])))
        try:
            left_margin = next(right_sorted)
            while left_margin[1] < newInterval[0]:
                left_margin = next(right_sorted)
            left_sorted = iter(reversed(intervals))
            right_margin = next(left_sorted)
            while right_margin[0] > newInterval[1]:
                right_margin = next(left_sorted)

            all_intervals.add((min(left_margin[0], newInterval[0]), max(right_margin[1], newInterval[1])))

            while left_margin != right_margin:
                all_intervals.remove(tuple(right_margin))
                right_margin = next(left_sorted)
            else:
                all_intervals.remove(tuple(right_margin))

            return list([list(t) for t in all_intervals])
        except StopIteration:
            return [newInterval]
