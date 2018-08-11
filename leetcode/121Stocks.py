class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        last_min = float("inf")
        profit = 0
        for v in prices:
            if v < last_min:
                last_min = v
            if v - last_min > profit:
                profit = v - last_min

        return profit





input = [7,1,5,3,6,4]

print(Solution().maxProfit(input))

# print(Solution().maxProfit(input2))