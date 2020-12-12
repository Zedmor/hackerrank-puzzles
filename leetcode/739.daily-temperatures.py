#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (63.99%)
# Total Accepted:    192.4K
# Total Submissions: 300.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
#
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
#
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#
#
import bisect
from collections import defaultdict
from typing import List


class Solution:
    """
    >>> Solution().dailyTemperatures([76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76])
    [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]

    >>> Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70])
    [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]

    >>> Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    [1, 1, 4, 2, 1, 1, 0, 0]
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        index_lookup = defaultdict(list)
        ordered_list = []
        for i, v in enumerate(T):
            index_lookup[v].append(i)
            index = bisect.bisect_left(ordered_list, v)
            for el in ordered_list[:index]:
                for target in index_lookup[el]:
                    result[target] = i - target
                index_lookup[el] = []
            ordered_list = ordered_list[index:]
            if len(index_lookup[v]) == 1:
                bisect.insort(ordered_list, v)
        return result

