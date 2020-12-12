#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (45.88%)
# Total Accepted:    265.8K
# Total Submissions: 576.7K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#
#
from functools import lru_cache
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_sets = set()

        @lru_cache(maxsize=1024)
        def recur(numbers):
            all_sets.add(tuple(sorted(numbers)))
            if len(numbers) == 1:
                all_sets.add(tuple())
                return
            for i in range(len(numbers)):
                recur(tuple(numbers[:i] + numbers[1+i:]))

        recur(tuple(nums))
        return [list(s) for s in all_sets]


print(Solution().subsetsWithDup([1,4,3,5,4,4,7,7,8,0]))
#
# z = [4,4,4,1,4]
#
# assert Solution().subsetsWithDup(z) == [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
