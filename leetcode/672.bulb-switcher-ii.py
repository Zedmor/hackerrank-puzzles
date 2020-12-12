#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#
# https://leetcode.com/problems/bulb-switcher-ii/description/
#
# algorithms
# Medium (51.03%)
# Total Accepted:    13.4K
# Total Submissions: 26.4K
# Testcase Example:  '1\n1'
#
# There is a room with n lights which are turned on initially and 4 buttons on
# the wall. After performing exactly m unknown operations towards buttons, you
# need to return how many different kinds of status of the n lights could be.
#
# Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4
# buttons are given below:
#
#
# Flip all the lights.
# Flip lights with even numbers.
# Flip lights with odd numbers.
# Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
#
#
#
#
# Example 1:
#
#
# Input: n = 1, m = 1.
# Output: 2
# Explanation: Status can be: [on], [off]
#
#
#
#
# Example 2:
#
#
# Input: n = 2, m = 1.
# Output: 3
# Explanation: Status can be: [on, off], [off, on], [off, off]
#
#
#
#
# Example 3:
#
#
# Input: n = 3, m = 1.
# Output: 4
# Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off],
# [off, on, on].
#
#
#
#
# Note: n and m both fit in range [0, 1000].
#
#
class Solution:
    """
    >>> Solution().flipLights(n = 1000, m = 1000)
    8

    >>> Solution().flipLights(n = 1, m = 1)
    2

    >>> Solution().flipLights(n = 2, m = 1)
    3

    >>> Solution().flipLights(n = 3, m = 1)
    4

    # Flip all the lights.
    # Flip lights with even numbers.
    # Flip lights with odd numbers.
    # Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

    """
    def flipLights(self, n: int, m: int) -> int:
        n = min(n, 6)
        dp = set([tuple([1] * n)])
        for i in range(m):
            new_dp = set()
            for variant in dp:
                new_dp.add(tuple([1 - e for e in variant]))
                new_dp.add(tuple([abs(1 - i % 2 - e) for i, e in enumerate(variant)]))
                new_dp.add(tuple([abs(1 - ((i + 1) % 2) - e) for i, e in enumerate(variant)]))
                new_dp.add(tuple([abs(int(i % 3 == 0) - e) for i, e in enumerate(variant)]))
            dp = new_dp

        return len(dp)



