"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftstart = 0
        leftend = len(nums) - 1
        leftfound = False
        rightend = len(nums) - 1
        rightstart = 0
        rightfound = False

        if not nums:
            return [-1, -1]
        while leftstart <= leftend and rightstart <= rightend and (not
                leftfound or not rightfound):

            leftmid = (leftstart + leftend) // 2
            if nums[leftmid] == target and (leftmid == 0 or nums[leftmid - 1] <
                target):
                leftfound = True
            else:
                if target <= nums[leftmid]:
                    leftend = leftmid - 1
                else:
                    leftstart = leftmid + 1
            rightmid = (rightstart + rightend) // 2
            if nums[rightmid] == target and (rightmid == len(nums) - 1 or nums[
                    rightmid + 1] >
                target):
                rightfound = True
            else:
                if target < nums[rightmid]:
                    rightend = rightmid - 1
                else:
                    rightstart = rightmid + 1

        return ([leftmid, rightmid]) if leftfound and rightfound else [-1, -1]

        # if nums[(leftstart+leftend) //2] >= target:
        #     leftend = (leftstart+leftend) //2
        #
        # if nums[(leftstart+leftend) //2] < target:
        #     leftstart = (leftstart+leftend) //2
        #
        #
        # if nums[(rightend+rightstart)//2] > target:
        #     rightend = (rightend+rightstart)//2
        # if nums[(rightend+rightstart)//2] <= target:
        #     rightstart = (rightend+rightstart)//2
        #
        # try:
        #     if nums[(leftstart + leftend) // 2+1] == target and nums[(
        #                 leftstart + leftend) // 2] < target:
        #         left = (leftstart + leftend) // 2+1
        # except IndexError:
        #     pass
        #
        # try:
        #     if nums[(rightstart + rightend) // 2 + 1] > target andbbi nums[(
        #                 rightstart + rightend) // 2] == target:
        #         right = (rightstart + rightend) // 2
        # except IndexError:
        #     pass
        #
        # if nums[left]==target and nums[right]==target:
        #     return [left, right]
        # #
        # # if (rightstart + rightend) // 2 == (leftstart + leftend) // 2:
        # #     return [-1, -1]


print(Solution().searchRange([5,7,7,8,8,10], 8))
