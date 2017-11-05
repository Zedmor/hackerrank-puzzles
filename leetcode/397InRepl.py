class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        best_result = float("Inf")
        def recur_find(n, depth=0):
            if n == 1:
                return depth
            if n % 2 == 0:
                d1 = recur_find(n / 2, depth + 1)
            d2 = recur_find(n - 1, depth + 1)
            d3 = recur_find(n + 1, depth + 1)
            print(d1, d2, d3)

        return recur_find(n)


print(Solution().integerReplacement(10000))
