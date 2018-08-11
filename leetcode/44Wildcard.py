class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


def test1():
    """Explanation: "a" does not match the entire string "aa"."""
    s = "aa"
    p = "a"
    assert not Solution().isMatch(s, p)


def test2():
    """
    Output: true
    Explanation: '*' matches any sequence.
    """
    s = "aa"
    p = "*"
    assert Solution().isMatch(s, p)


def test3():
    """
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
    """
    s = "cb"
    p = "?a"
    assert not Solution().isMatch(s, p)


def test4():
    """
    The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
    """
    s = "adceb"
    p = "*a*b"
    assert Solution().isMatch(s, p)


def test5():
    s = "acdcb"
    p = "a*c?b"
    assert not Solution().isMatch(s, p)
