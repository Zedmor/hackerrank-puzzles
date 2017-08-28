"""
Total Accepted: 113159
Total Submissions: 476385
Difficulty: Easy
Contributors: Admin
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for iteration in range(k):
        for index in range(k):
            nums[index], nums[index+k] = nums[index+k], nums[index]
        print(nums)

print(Solution().rotate([1,2,3,4,5,6,7,8,9,10], 3))