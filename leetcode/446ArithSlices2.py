from collections import defaultdict


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        dp = [defaultdict(int) for i in range(len(A))]
        res = 0
        for i in range(1, len(A)):
            for j in range(i):
                step = A[i]-A[j]
                dp[i][step] += 1
                if step in dp[j]:
                    dp[i][step]+= dp[j][step]
                    res += dp[j][step]
        return res


inp = [2, 4, 6, 8, 10]
print(Solution().numberOfArithmeticSlices(inp))
