"""
>>> Solution().mySqrt(8)
2

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        starting_range = (0, x // 2 + 1)
        while True:
            middle = (starting_range[1] - starting_range[0]) // 2
            if middle * middle > x:
                starting_range = (starting_range[0], middle)
            elif middle * middle < x:
                starting_range = (middle, starting_range[1])
            else:
                return middle
