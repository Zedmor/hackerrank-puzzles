from leetcode.Insert35 import Solution


def test1():
    assert 2 == Solution().searchInsert([1, 3, 5, 6], 5)

def test2():
    assert 1 == Solution().searchInsert([1, 3, 5, 6], 2)

def test3():
    assert 4 == Solution().searchInsert([1, 3, 5, 6], 7)

def test4():
    assert 0 == Solution().searchInsert([1, 3, 5, 6], 0)

def test5():
    assert 0 == Solution().searchInsert([1, 3, 5], 1)