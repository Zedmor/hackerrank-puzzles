"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

>>> Solution().uniquePaths(23, 12)
193536720


>>> Solution().uniquePaths(1, 1)
1


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

>>> Solution().uniquePaths(3, 2)
3

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

>>> Solution().uniquePaths(7, 3)
28

"""
from collections import defaultdict
from copy import copy


def create_graph(m, n):
    graph = defaultdict(list)

    def fit_coords(coords):
        return 0 <= coords[0] < m and 0 <= coords[1] < n

    for i in range(m):
        for j in range(n):
            adjestent_coords = [(i - 1, j), (i, j - 1)]
            adjestent_coords = list(filter(fit_coords, adjestent_coords))
            graph[(i, j)] = adjestent_coords

    if m == 1 and n == 1:
        graph[(0, 0)] = [(0, 0)]

    return graph




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        solution = [[None for x in range(m)] for y in range(n)]
        solution[n - 1][m - 1] = 1
        stack = []

        for i in range(n - 1, - 1, -1):
            for j in range(m - 1, - 1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                stack.append((i, j))
        while stack:
            i, j = stack.pop(0)
            down_value = solution[i + 1][j] if i + 1 < n else 0
            right_value = solution[i][j + 1] if j + 1 < m else 0

            if down_value is not None and right_value is not None:
                solution[i][j] = down_value + right_value
            else:
                stack.append((i, j))

        return solution[0][0]

