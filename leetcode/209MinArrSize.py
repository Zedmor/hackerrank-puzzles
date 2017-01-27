'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        best = float('inf')
        leftpointer = 0
        rightpointer = 0
        lennums = len(nums)
        runningsum = 0#nums[leftpointer]
        while rightpointer < lennums:
            while runningsum < s and rightpointer < lennums:
                rightpointer += 1
                runningsum += nums[rightpointer-1]
            while runningsum-nums[leftpointer] >= s:
                #sum(nums[leftpointer + 1:rightpointer])
                leftpointer += 1
                runningsum -= nums[leftpointer-1]
            if rightpointer - leftpointer < best and runningsum >= s:
                best = rightpointer - leftpointer
            leftpointer += 1
            runningsum -= nums[leftpointer - 1]
            #rightpointer = leftpointer
        return best if best != float('inf') else 0


a = Solution()
print(a.minSubArrayLen(80, [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]))
