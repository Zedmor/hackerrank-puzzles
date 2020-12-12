#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (53.66%)
# Total Accepted:    74.2K
# Total Submissions: 138.2K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given an integer array nums, return the maximum result of nums[i] XOR
# nums[j], where 0 ≤ i ≤ j < n.
#
# Follow up: Could you do this in O(n) runtime?
#
#
# Example 1:
#
#
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
#
# Example 2:
#
#
# Input: nums = [0]
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [2,4]
# Output: 6
#
#
# Example 4:
#
#
# Input: nums = [8,10,2]
# Output: 10
#
#
# Example 5:
#
#
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# 0 <= nums[i] <= 2^31 - 1
#
#
#
from typing import List


class Trie:
    def __init__(self):
        self.t = {}

    def put(self, n):
        cursor = self.t
        for i in n:
            cursor = cursor.setdefault(i, {})

    def get_max(self, bn):
        inv = {'1': '0', '0': '1'}
        cur = self.t
        result = []
        for c in bn:
            if inv[c] in cur:
                result.append('1')
                cur = cur[inv[c]]
            else:
                result.append('0')
                cur = cur[c]
        return int(''.join(result), 2)





class Solution:
    """
    >>> Solution().findMaximumXOR([89,102,183,233,175,87,497,350,348,191,136,497,166,420,279,212,269,125,262,74])
    28


    >>> Solution().findMaximumXOR([3,10,5,25,2,8])
    28

    >>> Solution().findMaximumXOR([0])
    0

    >>> Solution().findMaximumXOR([2,4])
    6

    >>> Solution().findMaximumXOR([8,10,2])
    10

    >>> Solution().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70])
    127

    """

    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        if not nums:
            return 0
        if len(nums) == 1:
            return 0

        max_result = 0
        trie.put(bin(nums[0])[2:].zfill(32))
        for n in nums[1:]:
            bn = bin(n)[2:].zfill(32)
            if trie.get_max(bn) > max_result:
                max_result = trie.get_max(bn)
            trie.put(bn)
        return max_result






