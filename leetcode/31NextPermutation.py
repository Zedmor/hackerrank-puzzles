"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class Solution:
    def get_rank(self, nums):
        original = sorted(nums)
        s = 0
        for v in nums:
            s += original.index(v) * factorial(len(original) - 1)
            original.remove(v)
        return s

    def get_permutation(self, rank, nums):
        if not nums:
            return []
        n = len(nums)
        char_idx = rank // factorial(n - 1)
        this_char = nums.pop(char_idx)
        return [this_char] + self.get_permutation(rank % factorial(n - 1), nums)

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        rank = self.get_rank(nums)
        try:
            return self.get_permutation(rank + 1, sorted(nums))
        except IndexError:
            return self.get_permutation(0, sorted(nums))


input = [3, 2, 1]
print(Solution().nextPermutation(input))
