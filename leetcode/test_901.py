from pytest import mark

from leetcode.online_stock_span_901 import StockSpanner

parameters = [
    ([100, 80, 60, 70, 60, 75, 85],
     [1, 1, 1, 2, 1, 4, 6]),
    ([31, 41, 48, 59, 79],
     [1, 2, 3, 4, 5]),
    ([29, 91, 62, 76, 51],
     [1, 2, 1, 2, 1])
]

@mark.parametrize("test_input, expected", parameters)
def test_spanner(test_input, expected):
    obj = StockSpanner()
    results = list(map(obj.next, test_input))
    print(results, expected)
    assert results == expected
