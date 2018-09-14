"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> Solution().maxSubArray([1])
        1
        >>> Solution().maxSubArray([-1])
        -1
        >>> Solution().maxSubArray([1,-1,1])
        1
        """
        if not nums:
            return
        max_sum = nums[0]
        running_sum = 0
        for num in nums:
            running_sum += num
            if running_sum > max_sum:
                max_sum = running_sum
            if running_sum < 0:
                running_sum = 0
        return max_sum
