#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
#
# algorithms
# Medium (66.02%)
# Total Accepted:    15.9K
# Total Submissions: 24.1K
# Testcase Example:  '[3,3,3,3,5,5,5,2,2,7]'
#
# Given an array arr.  You can choose a set of integers and remove all the
# occurrences of these integers in the array.
#
# Return the minimum size of the set so that at least half of the integers of
# the array are removed.
#
#
# Example 1:
#
#
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
# size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array
# [3,3,3,3,5,5,5] which has size greater than half of the size of the old
# array.
#
#
# Example 2:
#
#
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the
# new array empty.
#
#
# Example 3:
#
#
# Input: arr = [1,9]
# Output: 1
#
#
# Example 4:
#
#
# Input: arr = [1000,1000,3,7]
# Output: 1
#
#
# Example 5:
#
#
# Input: arr = [1,2,3,4,5,6,7,8,9,10]
# Output: 5
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# arr.length is even.
# 1 <= arr[i] <= 10^5
#
#
from collections import Counter
from typing import List


class Solution:
    """
    >>> Solution().minSetSize([3,3,3,3,5,5,5,2,2,7])
    2

    >>> Solution().minSetSize([7,7,7,7,7,7])
    1

    >>> Solution().minSetSize([1,9])
    1

    >>> Solution().minSetSize([1000,1000,3,7])
    1

    >>> Solution().minSetSize([1,2,3,4,5,6,7,8,9,10])
    5
    """
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        items_removed = 0
        size_of_the_set = 0
        sorted_items = sorted(c.values(), reverse=True)
        while sorted_items and items_removed < len(arr) // 2:
            count = sorted_items.pop(0)
            items_removed += count
            size_of_the_set += 1
        return size_of_the_set


