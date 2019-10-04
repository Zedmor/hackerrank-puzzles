"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

>>> Solution().uniquePathsWithObstacles([[1]])
0

Input:
>>> Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
2

Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
from collections import defaultdict
from copy import copy


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        n = len(obstacleGrid)
        if n > 0:
            m = len(obstacleGrid[0])

        stack = []

        for i in range(n - 1, - 1, -1):
            for j in range(m - 1, - 1, -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue

                if i == n - 1 and j == m - 1:
                    obstacleGrid[i][j] = 1
                    continue

                stack.append((i, j))

        while stack:
            i, j = stack.pop(0)
            down_value = obstacleGrid[i + 1][j] if i + 1 < n else 0
            right_value = obstacleGrid[i][j + 1] if j + 1 < m else 0

            if down_value is not None and right_value is not None:
                obstacleGrid[i][j] = down_value + right_value
            else:
                stack.append((i, j))
        return obstacleGrid[0][0]

