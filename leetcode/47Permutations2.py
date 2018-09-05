import random


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recur_perm(nums):
            if len(nums) == 1:
                return nums
            result = []
            for i, el in enumerate(nums):
                output = recur_perm(nums[:i] + nums[i + 1:])
                if output and type(output[0]) == list:
                    for sublist in output:
                        result.append([el] + sublist)
                else:
                    result.append([el] + output)

            return result
        all_r = set()
        res = recur_perm(nums)
        if res and type(res[0]) != list:
            return [res]
        for r in res:
            all_r.add(tuple(r))
        all_r = [list(s) for s in all_r]
        print(all_r)
        return all_r



inp = [1, 1, 2]
out = Solution().permuteUnique(inp)
print(out)
print(Solution().permuteUnique([1]))

assert [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
] == out
