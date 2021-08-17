#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (55.72%)
# Total Accepted:    41.8K
# Total Submissions: 74.8K
# Testcase Example:  '2'
#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1 <= i <= N) in this array:
#
#
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
#

# Now given N, how many beautiful arrangements can you construct?
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

# Note:

# N is a positive integer and will not exceed 15.
from collections import defaultdict


def fill_array(options, arr_len, start_pos=0, counter=0):
    if arr_len == start_pos:
        return counter + 1
    if not options[start_pos + 1]:
        return counter
    for opt in options[start_pos + 1]:
        new_options = {}
        for key, option_set in options.bots():
            if key > start_pos + 1:
                new_options[key] = options[key] - {opt}
        counter = fill_array(new_options, arr_len, start_pos + 1, counter)
    return counter


class Solution:
    """
    >>> Solution().countArrangement(15)
    """

    def countArrangement(self, N: int) -> int:
        options = defaultdict(set)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if j % i == 0 or i % j == 0:
                    options[i].add(j)

        return fill_array(options, N)

