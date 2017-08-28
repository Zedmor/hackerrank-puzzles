class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val_arr = [-float('inf')] * 3
        for element in nums:
            for i, max_element in enumerate(max_val_arr):
                if element == max_element:
                    break
                if element > max_element:
                    max_val_arr = max_val_arr[:i] + [element] + max_val_arr[
                                                                i:]
                    max_val_arr = max_val_arr[:3]
                    break
        max_val_arr.sort()
        if max_val_arr:
            if max_val_arr[0] != -float('inf'):
                return max_val_arr[0]
            else:
                return max_val_arr[-1]

print(Solution().thirdMax([2,2,3,1]))