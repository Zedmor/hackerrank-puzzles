#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (46.71%)
# Total Accepted:    249.7K
# Total Submissions: 534.4K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two  strings  S  and T,  return if they are equal when both are typed into
# empty text editors. # means a backspace character.
#
# Note that after  backspacing an empty text, the text will continue empty.
#
#
# Example 1:
#
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
#
#
# Example 2:
#
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
#
#
# Example 3:
#
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
#
#
# Example 4:
#
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
#
# Note:
#
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S  and T only contain  lowercase letters and '#' characters.
#
#
# Follow up:
#
#
# Can you solve it in O(N) time and O(1) space?
#
#
#
#
#
#
#
class Solution:
    """
    >>> Solution().backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp#######")
    False

    >>> Solution().backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp######")
    False

    >>> Solution().backspaceCompare("abcd", "bbcd")
    False

    >>> Solution().backspaceCompare("aaa###a", "aaaa###a")
    False

    >>> Solution().backspaceCompare("rheyggodcclgstf", "#rheyggodcclgstf")
    True

    >>> Solution().backspaceCompare("bbbextm", "bbb#extm")
    False

    >>> Solution().backspaceCompare("c##vnvr", "#c##vnvr")
    True

    >>> Solution().backspaceCompare("j##xfix", "j###xfix")
    True

    >>> Solution().backspaceCompare("y#fo##f", "y#fx#o##f")
    True

    >>> Solution().backspaceCompare("bxj##tw", "bxj###tw")
    False

    >>> Solution().backspaceCompare("bxj##tw", "bxo#j##tw")
    True

    >>> Solution().backspaceCompare(S = "a#c", T = "b")
    False

    >>> Solution().backspaceCompare(S = "ab#c", T = "ad#c")
    True

    >>> Solution().backspaceCompare(S = "ab##", T = "c#d#")
    True

    >>> Solution().backspaceCompare(S = "a##c", T = "#a#c")
    True

    """
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = [S, T]
        counters = [0, 0]
        while any([st for st in s]):
            for i in (0, 1):
                if all(c == 0 for c in counters):
                    if s[0] == s[1]:
                        return True
                    if not s[0] and s[1] and not s[1].endswith('#'):
                        return False
                    if not s[1] and s[0] and not s[0].endswith('#'):
                        return False

                if s[i] and s[i][-1] == '#':
                    counters[i] += 1
                    s[i] = s[i][:-1]
                elif counters[i] > 0:
                    if s[i] and s[i][-1] != '#':
                        s[i] = s[i][:-1]
                    counters[i] -= 1
                if all([c == 0 for c in counters]) and not s[0].endswith('#') and not s[1].endswith('#'):
                    if s[0] == s[1]:
                        return True
                    if (s[i] and not s[1 - i]) or (s[1 - i] and not s[i]):
                        return False
                    if s[i][-1] != s[1 - i][-1]:
                        return False
                    else:
                        s[i] = s[i][:-1]
                        s[1 - i] = s[1 - i][:-1]

        return s[0] == s[1]
