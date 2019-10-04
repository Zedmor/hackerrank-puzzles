"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
"""
from itertools import permutations

class Solution(object):
    """
    >>> Solution().getPermutation(3, 3)
    '213'
    """
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        perms = list(permutations(range(1, n + 1)))
        return ''.join(map(str, perms[k - 1]))

