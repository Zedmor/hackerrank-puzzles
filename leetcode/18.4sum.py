#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (32.89%)
# Total Accepted:    316.5K
# Total Submissions: 958K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
from collections import Counter, defaultdict
from copy import copy
from functools import lru_cache
from itertools import combinations, permutations, product
from typing import List


class Solution:
    """
    # >>> Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    # [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]

    >>> Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11)
    [[-5, -4, -3, 1]]

    >>> Solution().fourSum([-489,-487,-471,-464,-451,-421,-414,-405,-396,-355,-354,-350,-336,-335,-334,-307,-298,-296,-295,287,-267,-256,-247,-231,-170,-130,-120,-109,-96,-80,-78,-71,-63,-56,-44,-43,-13,2,9,18,31,36,39,43,49,49,50,61,68,73,99,107,112,13,120,121,173,180,185,190,203,210,233,246,258,296,319,340,345,370,371,378,395,418,436,444,447,451,460,485],2926)
    [[-5, -4, -3, 1]]

    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def create_two_element_sums(nums):
            sums = defaultdict(list)
            for combo in combinations(nums, 2):
                sums[sum(combo)].append(combo)
            return sums

        def create_element_to_two_elements_lookup(nums, sums):
            three_sums = defaultdict(list)
            for combo in product(nums, sums.keys()):
                three_sums[sum(combo)].append(combo)
            return three_sums

        value_counts = Counter(nums)
        if not value_counts:
            return []
        elements, counts = zip(*value_counts.items())
        value_to_element_index_map = {v: k for k, v in enumerate(elements)}
        variants = set()

        two_elements_sums = create_two_element_sums(nums)

        three_element_sums = create_element_to_two_elements_lookup(nums, two_elements_sums)

        @lru_cache(maxsize=1024)
        def search(counter, solution):
            if len(solution) == 1:
                last_target = target - sum(solution)
                for variant in three_element_sums.get(last_target, []):
                    if counter[value_to_element_index_map[variant[0]]] > 0:
                        new_counter = list(counter)
                        new_counter[value_to_element_index_map[variant[0]]] -= 1
                        search(tuple(new_counter), tuple(list(solution) + [variant[0]]))

            if len(solution) == 2:
                last_target = target - sum(solution)
                for variant in two_elements_sums.get(last_target, []):
                    vc = Counter(variant)
                    if all(counter[value_to_element_index_map[t]] >= vc[t] for t in variant):
                        variants.add(tuple(sorted(list(solution) + list(variant))))

            if len(solution) > 1:
                return
            else:
                for i, count in enumerate(counter):
                    if count > 0:
                        new_counter = list(counter)
                        new_counter[i] -= 1
                        search(tuple(new_counter), tuple(sorted(list(solution) + [elements[i]])))

        search(tuple(counts), tuple())

        return [list(v) for v in variants]
