class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n+2)
        a[0] = 1
        a[1] = 2
        for i in range(2,n):
            a[i] = a[i-1] + a[i-2]
        return a[n-1]


a = Solution()
print(a.climbStairs(4))