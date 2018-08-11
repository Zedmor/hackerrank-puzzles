class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left_pointer = 0
        new_len = len(nums)
        right_pointer = len(nums) - 1
        if left_pointer==right_pointer and nums[0] == val:
            return 0
        while left_pointer <= right_pointer:
            while left_pointer <= right_pointer and nums[left_pointer] == val and right_pointer > -1:
                while left_pointer <= right_pointer and nums[right_pointer] == val:
                    right_pointer -= 1
                    new_len -= 1
                    if right_pointer == -1:
                        break
                if left_pointer < right_pointer:
                    nums[left_pointer] = nums[right_pointer]
                    new_len -= 1
                    right_pointer -= 1
                left_pointer += 1
            left_pointer += 1
        print(nums)
        return new_len



nums = [0,4,4,0,4,4,4,0,2]
val = 4
print(Solution().removeElement(nums, val))
