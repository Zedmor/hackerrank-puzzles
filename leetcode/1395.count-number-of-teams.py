#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#
# https://leetcode.com/problems/count-number-of-teams/description/
#
# algorithms
# Medium (82.02%)
# Total Accepted:    39.4K
# Total Submissions: 48K
# Testcase Example:  '[2,5,3,4,1]\r'
#
# There are n soldiers standing in a line. Each soldier is assigned a unique
# rating value.
#
# You have to form a team of 3 soldiers amongst them under the following
# rules:
#
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
# rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] >
# rating[j] > rating[k]) where (0 <= i < j < k < n).
#
#
# Return the number of teams you can form given the conditions. (soldiers can
# be part of multiple teams).
#
#
# Example 1:
#
#
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1),
# (5,3,1).
#
#
# Example 2:
#
#
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
#
#
# Example 3:
#
#
# Input: rating = [1,2,3,4]
# Output: 4
#
#
#
# Constraints:
#
#
# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5
#
#
import bisect
from collections import defaultdict
from typing import List


class Solution:
    """
    >>> Solution().numTeams([69397,24321,95357,15446,48370,45242,61027,78457,40678,59832,54721,38394,24003,32951,94919,41829,3563,26440,99784,53252,55184,36578,38285,53660,88702,12043,88612,7653,19333,54706,37751,88308,36114,72823,88869,27749,56744,51290,14902,74919,71923,79364,43462,12325,66301,75561,70887,35542,37160,1823,35530,97666,58620,83080,51800,43742,46349,67223,30060,56415,66180,57141,32195,6416,93874,15276,66229,55568,85670,19526,75450,68451,30104,84901,29873,38875,90795,72998,30214,80296,72365,38649,49855,55730,21509,31712,81480,38733,62792,19769,8440,17184,59427,1499,18792,87260,4349,77118,13261,1432,51984,82976,59700,2383,55631,83002,46570,23082,77029,24113,11671,58877,39369,57054])
    80486

    >>> Solution().numTeams([2,5,3,4,1])
    3

    >>> Solution().numTeams([2,1,3])
    0

    >>> Solution().numTeams([1,2,3,4])
    4

    """
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        groups = {}
        for item in rating:
            groups[item] = {'inc': [[item]], 'dec': [[item]]}

            for key in groups.keys():
                if key < item:
                    for group in groups[key]['inc']:
                        if len(group) < 3:
                            groups[item]['inc'].append(group + [item])
                            if len(group) == 2:
                                counter += 1

                if key > item:
                    for group in groups[key]['dec']:
                        if len(group) < 3:
                            groups[item]['dec'].append(group + [item])
                            if len(group) == 2:
                                counter += 1

        return counter




