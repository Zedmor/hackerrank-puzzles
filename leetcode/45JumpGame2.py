"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for i, value in enumerate(nums):
            for j in range(1, value + 1):
                if i+j < len(nums):
                    graph[i].append(i+j)

        visited = set()

        q = [(0, 0, ())]

        while q:
            (cost, v1, path) = heappop(q)
            if v1 not in visited:
                visited.add(v1)
                path = (v1, path)
                if v1 == len(nums) -1:
                    return cost
                for v2 in graph[v1]:
                    if v2 not in visited:
                        heappush(q, (cost+ 1, v2, path))
        return float("inf")


inp = [2,3,1,1,4]
print(Solution().jump(inp))
