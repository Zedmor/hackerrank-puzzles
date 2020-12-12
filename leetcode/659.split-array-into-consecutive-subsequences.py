#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (43.05%)
# Total Accepted:    38.2K
# Total Submissions: 88.7K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# Given an array nums sorted in ascending order, return true if and only if you
# can split it into 1 or more subsequences such that each subsequence consists
# of consecutive integers and has length at least 3.
#
#
#
# Example 1:
#
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
#
#
#
# Example 2:
#
#
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
#
#
#
# Example 3:
#
#
# Input: [1,2,3,4,4,5]
# Output: False
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10000
#
#
#
#
#
from copy import deepcopy
from typing import List


class Solution:
    """

    # >>> Solution().isPossible([14,14,15,15,16,16,17,17,18,18,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,24,24,25,25,25,25,26,26,26,26,27,27,27,27,28,28,28,28,29,29,29,30,30,30,31,31,31,32,32,32,33,33,33,34,34,34,35,35,35,36,36,36,37,37,37,38,38,38,39,39,39,40,40,40,41,41,41,42,42,43,43,44,44,45,45,46,46,47,47,47,48,48,48,49,49,49,50,50,50,51,51,51,52,52,52,53,53,53,54,54,54,55,55,55,56,56,56,57,57,57,58,58,58,59,59,59,60,60,60,61,61,61,62,62,62,62,63,63,63,63,64,64,64,64,65,65,65,65,65,66,66,66,66,66,67,67,67,67,67,68,68,68,68,68,68,69,69,69,69,69,69,70,70,70,70,70,70,71,71,71,71,71,71,72,72,72,72,72,72,73,73,73,73,73,73,74,74,74,74,74,74,75,75,75,75,75,75,76,76,76,76,76,76,77,77,77,77,77,77,78,78,78,78,78,78,79,79,79,79,79,79,80,80,80,80,80,80,80,81,81,81,81,81,81,81,82,82,82,82,82,82,82,83,83,83,83,83,83,83,84,84,84,84,84,84,84,85,85,85,85,85,85,85,86,86,86,86,86,86,86,86,87,87,87,87,87,87,87,87,88,88,88,88,88,88,88,88,89,89,89,89,89,89,89,89,90,90,90,90,90,90,90,90,91,91,91,91,91,91,91,92,92,92,92,92,92,92,93,93,93,93,93,93,93,94,94,94,94,94,94,95,95,95,95,95,95,96,96,96,96,96,96,97,97,97,97,97,97,98,98,98,98,98,98,99,99,99,99,99,99,100,100,100,100,100,101,101,101,101,101,102,102,102,102,102,103,103,103,103,103,104,104,104,104,104,105,105,105,105,105,106,106,106,106,106,107,107,107,107,107,108,108,108,108,108,109,109,109,109,109,110,110,110,110,110,111,111,111,111,111,112,112,112,113,113,113,114,114,114,115,115,115,116,116,116,117,117,117,118,118,118,119,119,119,120,120,120,121,121,121,122,122,122,123,123,123,124,124,124,125,125,125,126,126,126,127,127,127,128,128,128,129,129,129,130,130,130,131,131,131,132,132,132,133,133,133,134,134,135,135,136,136,137,137,138,138,139,139,140,140,141,141,142,142,143,143,144,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170])
    # True


    >>> Solution().isPossible([1,2,3,3,4,5])
    True

    >>> Solution().isPossible([1,2,3,3,4,4,5,5])
    True

    >>> Solution().isPossible([1,2,3,4,4,5])
    False


    """


    def isPossible(self, nums: List[int]) -> bool:

        variants = set([frozenset()])

        while variants:
            pointer = 0
            variant = variants.pop()
            while pointer <= len(nums):
                if pointer == len(nums):
                    if variant and min([e[0] for e in variant]) >= 3 and sum([e[0] for e in variant]) \
                            == len(nums):
                        return True
                    break

                new_collector = set(deepcopy(variant))
                for item in deepcopy(variant):
                    new_collector.discard(item)
                    if item[1] == nums[pointer] - 1:
                        new_collector.add((item[0] + 1, nums[pointer]))
                        variants.add(frozenset(new_collector))

                new_collector = set(deepcopy(variant))
                new_collector.add((1, nums[pointer]))
                variants.add(frozenset(new_collector))

                # for collector in deepcopy(variants):
                #     if sum([e[0] for e in collector]) < pointer:
                #         variants.discard(collector)
                #     for item in collector:
                #         if item[1] < nums[pointer] - 1:
                #             if item[0] < 3:
                #                 variants.discard(collector)

                pointer += 1

