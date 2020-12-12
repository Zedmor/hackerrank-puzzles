#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (48.43%)
# Total Accepted:    52.9K
# Total Submissions: 108.9K
# Testcase Example:  '3'
#
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step:
#
#
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
#
#
#
#
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'.
#
# Example 1:
#
#
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#
#
#
#
# Note:
#
#
# The n will be in the range [1, 1000].
#
#
#
#
#
class Solution:
    """
    >>> Solution().minSteps(3)
    3

    >>> Solution().minSteps(25)
    3
    """

    def minSteps(self, n: int) -> int:
        def recur(a, buf, n_steps=0):
            if a == n:
                return n_steps
            if a > n:
                return float('inf')
            if buf == 0:
                return recur(a, a, n_steps + 1)
            if a != buf:
                return min(recur(a + buf, buf, n_steps + 1), recur(a, a, n_steps + 1))
            else:
                return recur(a + buf, buf, n_steps + 1)

        return recur(1, 0)
