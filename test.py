class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def fact(x):
            res = 1
            for i in range(1, x):
                res *= i + 1
            return res

        results = []
        for i in range(fact(len(nums))):
            for k in range(len(nums)-1):
                apermindex = i
                alist = nums
                apermindex, j = divmod(apermindex, len(alist) - i)
                alist[k], alist[k + j] = alist[k + j], alist[k]
            results.append(alist)
        return results

a = Solution()
print(a.permute([1,2,3]))