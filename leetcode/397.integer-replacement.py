#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#
# https://leetcode.com/problems/integer-replacement/description/
#
# algorithms
# Medium (31.91%)
# Total Accepted:    51.4K
# Total Submissions: 158.4K
# Testcase Example:  '8'
#
#
# Given a positive integer n and you can do operations as follow:
#
#
#
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
#
#
#
#
# What is the minimum number of replacements needed for n to become 1?
#
#
#
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
#
#
#
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#
#
#
import heapq
from collections import defaultdict


class Solution:
    """
    >>> Solution().integerReplacement(2147483647)
    17

    >>> Solution().integerReplacement(65535)
    17

    >>> Solution().integerReplacement(8)
    3

    >>> Solution().integerReplacement(7)
    4
    """

    def integerReplacement(self, n: int) -> int:
        """
        If n is even, replace n with n/2.
        If n is odd, you can replace n with either n + 1 or n - 1.

        What is the minimum number of replacements needed for n to become 1?
        """
        distances = defaultdict(lambda: float('inf'))

        distances[n] = 0

        heap = [(0, n)]

        visited = set()

        def possible_values(n):
            if n % 2 == 0:
                return [n // 2]
            else:
                return [n + 1, n - 1]

        while heap:
            current = heapq.heappop(heap)[1]
            if current in visited:
                continue
            for neighbour in possible_values(current):
                if neighbour not in visited:
                    new_distance = distances[current] + 1
                    if distances[neighbour] > new_distance:
                        distances[neighbour] = new_distance
                    heapq.heappush(heap, (new_distance, neighbour))
            visited.add(current)

        return distances[1]
