#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (59.08%)
# Total Accepted:    531.4K
# Total Submissions: 892.4K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#
from copy import copy
from functools import lru_cache
from typing import List


class Solution:
    """
    >>> Solution().subsets([1, 2, 3])
    [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]

    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = set()

        @lru_cache(maxsize=256)
        def recur(solution, arr):
            if len(arr) == 0:
                solutions.add(tuple())
                solutions.add(tuple(sorted(solution)))
            else:
                for i, item in enumerate(arr):
                    new_solution = list(solution)
                    new_arr = list(arr)
                    if new_arr[i] not in new_solution:
                        new_solution.append(new_arr.pop(i))
                        new_solution = tuple(sorted(new_solution))
                        solutions.add(new_solution)
                        recur(new_solution, tuple(new_arr))

        recur(tuple(), tuple(nums))

        return [list(i) for i in solutions]
