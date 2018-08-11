from leetcode.SearchInRotatedArr33 import Solution


def test1():
    assert 4 == Solution().search([4, 5, 6, 7, 0, 1, 2], 0)


def test2():
    assert -1 == Solution().search([4, 5, 6, 7, 0, 1, 2], 3)


def test3():
    assert -1 == Solution().search([], 5)


def test4():
    assert 5 == Solution().search([4, 5, 6, 7, 0, 1, 2], 1)


def test5():
    assert 1 == Solution().search([4, 5, 6, 7, 0, 1, 2], 5)


def test6():
    assert -1 == Solution().search([4, 5, 6, 7, 0, 1, 2], 8)


def test7():
    assert 3 == Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2)
