#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (49.41%)
# Total Accepted:    176.1K
# Total Submissions: 348.9K
# Testcase Example:  '[0,0,0,0]'
#
#
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
#
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
#
#
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
#
#
#
# Note:
#
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
#
#
#
from collections import defaultdict
from typing import List


class Solution:
    """
    >>> Solution().minCostClimbingStairs([10, 15, 20])
    15

    >>> Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    6
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(list)
        i = 0
        if len(cost) > 1:
            dp[1] = [cost[1]]
        if len(cost) > 0:
            dp[0] = [cost[0]]
        for i in range(len(cost)):
            dp[i] = min(dp[i])
            if i < len(cost) - 1:
                dp[i + 1].append(dp[i] + cost[i + 1])
            if i < len(cost) - 2:
                dp[i + 2].append(dp[i] + cost[i + 2])
        return min(dp[len(cost) - 1], dp[len(cost) - 2])

