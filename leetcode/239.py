"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        deque = [i[0] for i in sorted(enumerate(nums[:k]), key=lambda x: x[1])]
        res = [nums[deque[-1]]]
        for i in range(k, len(nums)):
            deque = [x for x in deque if x >= i - k+1]
            newelement = nums[i]
            deque = [x for x in deque if nums[x] > newelement]

            deque = [i] + deque
            res.append(nums[deque[-1]])

        return res


a = Solution()
nums = [9, 10, 9, -7, -4, -8, 2, -6]
k = 5
print(a.maxSlidingWindow(nums, k))
