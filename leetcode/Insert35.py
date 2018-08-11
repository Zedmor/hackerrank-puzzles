class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        center = (right - left) // 2 + left
        if target < nums[left]:
            return 0
        if target > nums[right]:
            return right + 1
        while left < right:
            center = (right - left) // 2 + left
            if nums[center] == target:
                return center
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if left + 1 == right:
                return right
            if nums[left] < target < nums[center]:
                right = center
            if nums[center] < target < nums[right]:
                left = center
        return center
