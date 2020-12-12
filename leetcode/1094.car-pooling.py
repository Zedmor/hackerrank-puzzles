#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#
# https://leetcode.com/problems/car-pooling/description/
#
# algorithms
# Medium (56.70%)
# Total Accepted:    25.6K
# Total Submissions: 45.2K
# Testcase Example:  '[[2,1,5],[3,3,7]]\n4'
#
# You are driving a vehicle that has capacity empty seats initially available
# for passengers.  The vehicle only drives east (ie. it cannot turn around and
# drive west.)
#
# Given a list of trips, trip[i] = [num_passengers, start_location,
# end_location] contains information about the i-th trip: the number of
# passengers that must be picked up, and the locations to pick them up and drop
# them off.  The locations are given as the number of kilometers due east from
# your vehicle's initial location.
#
# Return true if and only if it is possible to pick up and drop off all
# passengers for all the given trips. 
#
#
#
# Example 1:
#
#
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
#
#
#
# Example 2:
#
#
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
#
#
#
# Example 3:
#
#
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true
#
#
#
# Example 4:
#
#
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
#

# Constraints:
#
#
# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().carPooling([[45,478,721],[83,13,226],[84,360,714],[11,18,859],[8,10,503],[72,126,141],[39,45,293], [29,662,690],[19,93,439],[21,247,687],[86,266,700],[71,76,799],[28,198,378],[59,414,436],[61,221,918],[15,833,971],[37,765,864],[48,42,428],[61,285,907],[19,11,709],[83,16,113],[86,766,824],[72,63,426],[54,194,612],[46,443,472],[4,715,901],[65,167,213],[20,239,407],[6,244,269],[81,25,789],[86,82,714],[83,770,966],[67,211,894],[32,18,167],[60,398,836],[99,657,676],[67,518,727],[20,440,983],[79,70,159],[77,95,876],[58,323,518],[85,244,519],[17,470,753],[44,126,682],[93,758,926],[72,549,576],[79,39,481],[71,156,527],[86,158,381],[11,183,187],[3,5,359],[4,597,996],[64,290,585],[27,300,729],[1,219,949],[71,54,616],[99,828,885],[12,26,78],[39,462,884],[74,93,194],[32,55,174],[69,176,999],[96,114,877],[43,716,972],[12,332,349],[37,230,283],[21,478,752],[88,25,123],[88,231,413],[57,102,516],[100,242,709],[77,562,783],[88,396,721],[95,586,993],[29,43,934],[17,247,778],[47,528,644],[17,605,788],[31,570,990],[64,291,901],[12,500,620],[42,194,340],[43,380,826],[8,180,339],[91,134,777],[15,732,809],[78,348,666],[39,567,689],[84,298,668],[48,18,590],[2,59,709],[45,6,263],[55,717,874],[81,368,435],[8,302,882],[36,145,333],[71,304,865],[23,405,578],[88,440,746],[46,4,373]], 2644)
    True


    >>> Solution().carPooling([[2,1,5],[3,3,7]], 4)
    False

    >>> Solution().carPooling([[2,1,5],[3,3,7]], 5)
    True

    >>> Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11)
    True

    """
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        right_margin = max(trips, key=lambda t: t[2])[2]
        all_trips = [0 for x in range(right_margin)]
        for t in trips:
            for c in range(t[1], t[2]):
                all_trips[c] += t[0]
                if all_trips[c] > capacity:
                    return False
        return True




