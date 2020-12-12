#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#
# https://leetcode.com/problems/bag-of-tokens/description/
#
# algorithms
# Medium (40.24%)
# Total Accepted:    14.2K
# Total Submissions: 34.7K
# Testcase Example:  '[100]\n50'
#
# You have an initial power P, an initial score of 0 points, and a bag of
# tokens.
#
# Each token can be used at most once, has a value token[i], and has
# potentially two ways to use it.
#
#
# If we have at least token[i] power, we may play the token face up, losing
# token[i] power, and gaining 1 point.
# If we have at least 1 point, we may play the token face down, gaining
# token[i] power, and losing 1 point.
#
#
# Return the largest number of points we can have after playing any number of
# tokens.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: tokens = [100], P = 50
# Output: 0
#
#
#
# Example 2:
#
#
# Input: tokens = [100,200], P = 150
# Output: 1
#
#
#
# Example 3:
#
#
# Input: tokens = [100,200,300,400], P = 200
# Output: 2
#
#
#
#
# Note:
#
#
# tokens.length <= 1000
# 0 <= tokens[i] < 10000
# 0 <= P < 10000
#
#
#
#
#
#
from functools import lru_cache
from typing import List


class Solution:
    """
    >>> Solution().bagOfTokensScore([9429,3028,4080,8100,622,6409,1273,2870,8299,555,359,4178,4918,8633,7171], 6735)
    7

    >>> Solution().bagOfTokensScore([100], 50)
    0

    >>> Solution().bagOfTokensScore([100, 200], 150)
    1

    >>> Solution().bagOfTokensScore([100,200,300,400], 200)
    2

    """
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        max_score = 0
        score = 0
        while tokens:
            if tokens[0] <= P:
                P -= tokens.pop(0)
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                P += tokens.pop()
                score -= 1
            else:
                return max_score
        return max_score







