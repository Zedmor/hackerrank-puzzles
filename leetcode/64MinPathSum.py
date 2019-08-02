"""
>>> Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
7

"""

class Solution:
    def minPathSum(self, obstacleGrid) -> int:

        n = len(obstacleGrid)
        if n > 0:
            m = len(obstacleGrid[0])

        stack = []

        for i in range(n - 1, - 1, -1):
            for j in range(m - 1, - 1, -1):

                if i == n - 1 and j == m - 1:
                    continue

                stack.append((i, j))

        while stack:
            i, j = stack.pop(0)
            down_value = obstacleGrid[i + 1][j] if i + 1 < n else float('inf')
            right_value = obstacleGrid[i][j + 1] if j + 1 < m else float('inf')

            if down_value is not None and right_value is not None:
                obstacleGrid[i][j] = obstacleGrid[i][j] + min(down_value, right_value)
            else:
                stack.append((i, j))
        return obstacleGrid[0][0]