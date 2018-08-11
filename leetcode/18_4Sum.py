"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from collections import defaultdict

triplets = defaultdict(list)
duplets = defaultdict(list)

def cached(cache):
    def cached_with_argument(lookup_function):
        def wrapper(nums, target):
            if target in cache:
                return list(cache[target])
            else:
                result = tuple(lookup_function(nums, target))
                cache[target] = result
                return list(result)
        return wrapper
    return cached_with_argument

@cached(duplets)
def find_duplet(nums, target):
    result = []
    for i, n in enumerate(nums):
        if -n == target:
            result.append([n, target])
    return result

@cached(triplets)
def find_triplet(nums, target):
    result = []
    for i, n in enumerate(nums):
        duplet = find_duplet(array[:i] + array[i+1:], target - n)
        if result:
            result.append(duplet + [n])
    return result



class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i, n in enumerate(nums):
            triplet = find_triplet(array[:i] + array[i+1:], target - n)
            if triplet:
                result.append(triplet + [n])
        return result


array = [1, 0, -1, 0, -2, 2]

print(Solution().fourSum(array, 0))
