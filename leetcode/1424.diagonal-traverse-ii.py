#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#
# https://leetcode.com/problems/diagonal-traverse-ii/description/
#
# algorithms
# Medium (38.11%)
# Total Accepted:    11.1K
# Total Submissions: 27.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a list of lists of integers, nums, return all elements of nums in
# diagonal order as shown in the below images.
#
# Example 1:
#
#
#
#
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
#
#
# Example 2:
#
#
#
#
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#
#
# Example 3:
#
#
# Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# Output: [1,4,2,5,3,8,6,9,7,10,11]
#
#
# Example 4:
#
#
# Input: nums = [[1,2,3,4,5,6]]
# Output: [1,2,3,4,5,6]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= nums[i][j] <= 10^9
# There at most 10^5 elements in nums.
#
#
#
from typing import List


class Solution:
    """
    >>> Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
    [1, 4, 2, 7, 5, 3, 8, 6, 9]

    >>> Solution().findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]

    >>> Solution().findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]])
    [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]

    >>> Solution().findDiagonalOrder([[1,2,3,4,5,6]])
    [1, 2, 3, 4, 5, 6]
    """
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        def index_gerenator(arr, num_lens):
            diag = 0
            yield 0, 0
            while True:
                diag += 1
                counter = 0
                for i in range(diag, -1, -1):
                    if i >= len(nums):
                        continue
                    if diag - i >= num_lens[i]:
                        continue
                    counter += 1
                    yield i, diag - i
                if counter == 0:
                    break

        num_lens = {li: len(nums[li]) for li in range(len(nums))}
        it = index_gerenator(nums, num_lens)
        return [nums[i][j] for i, j in it]
