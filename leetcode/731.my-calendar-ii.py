#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# https://leetcode.com/problems/my-calendar-ii/description/
#
# algorithms
# Medium (46.19%)
# Total Accepted:    32.3K
# Total Submissions: 68.5K
# Testcase Example:  '["MyCalendarTwo","Book","Book","Book","Book","Book","Book"]\n[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# Implement a MyCalendarTwo class to store your events. A new event can be
# added if adding the event will not cause a triple booking.
#
# Your class will have one method, Book(int start, int end). Formally, this
# represents a booking on the half open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# A triple booking happens when three events have some non-empty intersection
# (ie., there is some time that is common to all 3 events.)
#
# For each call to the method MyCalendar.Book, return true if the event can be
# added to the calendar successfully without causing a triple booking.
# Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar();
# MyCalendar.Book(start, end)
#
# Example 1:
#
#
# MyCalendar();
# MyCalendar.Book(10, 20); // returns true
# MyCalendar.Book(50, 60); // returns true
# MyCalendar.Book(10, 40); // returns true
# MyCalendar.Book(5, 15); // returns false
# MyCalendar.Book(5, 10); // returns true
# MyCalendar.Book(25, 55); // returns true
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple
# booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is
# already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be
# double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double
# booked with the second event.
#
#
#
#
# Note:
#
#
# The number of calls to MyCalendar.Book per test case will be at most
# 1000.
# In calls to MyCalendar.Book(start, end), start and end are integers in the
# range [0, 10^9].
#
#
#
#
import bisect




class MyCalendarTwo:

    def __init__(self):
        self.intervals_end_sorted = []
        self.intervals_start_sorted = []


    def overlap(self, start, end):
        left_edge = bisect.bisect_left(self.intervals_end_sorted, (end, (start, end)))
        while self.intervals_end_sorted[left_edge][1][1]
        pass



    def book(self, start: int, end: int) -> bool:
        if not self.overlap(start, end):
            bisect.insort_left(self.intervals_start_sorted, (start, end))
            bisect.insort_left(self.intervals_end_sorted, (end, (start, end)))
            return True
        else:
            return False


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.Book(start,end)

c = MyCalendarTwo()
assert c.book(10, 20)
assert c.book(50, 60)
assert c.book(10, 40)
assert not c.book(5, 15)
assert c.book(25, 55)
