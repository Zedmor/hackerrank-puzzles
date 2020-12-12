#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (57.16%)
# Total Accepted:    10K
# Total Submissions: 17.5K
# Testcase Example:  '4'
#
# For some fixed N, an array A is beautiful if it is a permutation of the
# integers 1, 2, ..., N, such that:
#
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] +
# A[j].
#
# Given N, return any beautiful array A.  (It is guaranteed that one
# exists.)
#
# Example 1:
#
# Input: 4
# Output: [2,1,4,3]
#
# Example 2:
#
#
# Input: 5
# Output: [3,1,2,5,4]
#
# 1 <= N <= 1000
#
import itertools
from functools import lru_cache
from typing import List





class Solution:
    """
    >>> Solution().beautifulArray(4)
    [2,1,4,3]

    >>> Solution().beautifulArray(8)
    [3,1,2,5,4]

    """
    def beautifulArray(self, N: int) -> List[int]:
        @lru_cache(maxsize=1024)
        def variant_works(left_part, n, right_part):
            sums = {sum(p) for p in itertools.product(left_part, right_part)}
            return n * 2 not in sums


        @lru_cache(maxsize=1024)
        def find_good_places(v, n):
            results = []
            for position in range(len(v) + 1):
                if variant_works(v[:position], n, v[position:]):
                    new_variant = list(v[:position]) + [n] + list(v[position:])
                    results.append(new_variant)
            return results

        @lru_cache(maxsize=1024)
        def search(n):
            if n == 1:
                return [[1]]
            variants = search(n - 1)
            new_variants = []
            for v in variants:
                new_variants.extend(find_good_places(tuple(v), n))
            return new_variants

        return search(N)[0]


