#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
# https://leetcode.com/problems/course-schedule-iii/description/
#
# algorithms
# Hard (33.55%)
# Total Accepted:    24.6K
# Total Submissions: 73.2K
# Testcase Example:  '[[100,200],[200,1300],[1000,1250],[2000,3200]]'
#
# There are n different online courses numbered from 1 to n. Each course has
# some duration(course length) t and closed on dth day. A course should be
# taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
#
# Given n online courses represented by pairs (t,d), your task is to find the
# maximal number of courses that can be taken.
#
# Example:
#
#
# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation:
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the
# 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the
# 1100th day, and ready to take the next course on the 1101st day.
# Third, take the 2nd course, it costs 200 days so you will finish it on the
# 1300th day.
# The 4th course cannot be taken now, since you will finish it on the 3300th
# day, which exceeds the closed date.
#
#
#
#
# Note:
#
#
# The integer 1 <= d, t, n <= 10,000.
# You can't take two courses simultaneously.
#
#
#
#
#
import heapq
from functools import lru_cache
from typing import List


def filter_bag(bag, time, interval):

    return tuple([item for item in bag if item[1] >= time + item[0] and item != interval])


class Solution:
    """
    >>> Solution().scheduleCourse([[671,4420],[481,6286],[248,1026],[590,4427],[480,843],[208,5326],[1000,9443],[87,7434],[683,7547],[435,8617],[376,9563],[900,5643],[798,8797],[750,8705],[393,7240],[849,8602],[743,7803],[721,7094],[556,2574]])
    17

    >>> Solution().scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]])
    4

    >>> Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
    3

    """
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda t: t[1])
        heap = []
        running_count = 0
        for course in courses:
            heapq.heappush(heap, -course[0])
            running_count += course[0]
            if running_count > course[1]:
                top = heapq.heappop(heap)
                running_count -= -top
        return len(heap)



