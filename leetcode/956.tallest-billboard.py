#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
# https://leetcode.com/problems/tallest-billboard/description/
#
# algorithms
# Hard (38.52%)
# Total Accepted:    6.6K
# Total Submissions: 16.7K
# Testcase Example:  '[1,2,3,6]'
#
# You are installing a billboard and want it to have the largest height.  The
# billboard will have two steel supports, one on each side.  Each steel support
# must be an equal height.
#
# You have a collection of rods which can be welded together.  For example, if
# you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
#
# Return the largest possible height of your billboard installation.  If you
# cannot support the billboard, return 0.
#
#
#
# Example 1:
#
#
# Input: [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
# same sum = 6.
#
#
#
# Example 2:
#
#
# Input: [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
# same sum = 10.
#
#
#
#
# Example 3:
#
#
# Input: [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
#
#
#
#
#
# Note:
#
#
# 0 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# The sum of rods is at most 5000.
#
#
#
from typing import List


def subsetSum(input, target):
    row, col = len(input), target + 1
    db = [[False] * col for _ in range(row)]
    for i in range(row):
        db[i][0] = False

    for i in range(row):
        for j in range(i, col):
            if input[i] == j:
                db[i][j] = True
            elif i > 0:
                for r in range(i):
                    if j - input[i] > 0:
                        if db[r][j - input[i]]:
                            db[i][j] = True


    for j in range(col - 1, -1, -1):
        counter = 0
        for i in range(row):
            if db[i][j]:
                counter += 1
                if counter == 2:
                    return j



class Solution:
    """
    # >>> Solution().tallestBillboard([1,2,3,6])
    # 6

    # >>> Solution().tallestBillboard([1,2,3,4,5,6])
    # 10
    #
    # >>> Solution().tallestBillboard([1,2])
    # 0


    """

    def tallestBillboard(self, rods: List[int]) -> int:
        print(subsetSum(rods, 16))

Solution().tallestBillboard([1,2,3,4,5,6])
