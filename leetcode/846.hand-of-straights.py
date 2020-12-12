#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (52.60%)
# Total Accepted:    56.6K
# Total Submissions: 103.2K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size
# W, and consists of W consecutive cards.
#
# Return true if and only if she can.
#
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
#
#
# Example 1:
#
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
#
# Example 2:
#
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
#
#
#
#
# Constraints:
#
#
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
#
#
#
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List


class Solution:
    """
    >>> Solution().isNStraightHand(hand = [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11], W = 10)
    # True
    #
    >>> Solution().isNStraightHand(hand = [1], W = 1)
    True

    >>> Solution().isNStraightHand(hand = [1,2,3], W = 1)
    True

    >>> Solution().isNStraightHand(hand = [1,2,3,4,5,6], W = 2)
    True

    >>> Solution().isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], W = 3)
    True

    >>> Solution().isNStraightHand(hand = [1,2,3,4,5], W = 4)
    False

    """

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = Counter(hand)
        while counter:
            for x in range(min(counter.keys()), min(counter.keys()) + W):
                counter[x] -= 1
                if counter[x] < 0:
                    return False
                if counter[x] == 0:
                    del counter[x]
        return True


