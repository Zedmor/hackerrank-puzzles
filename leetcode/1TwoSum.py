'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numssorted = sorted(nums, key=lambda x:abs(x))
        #minelementindex = numssorted.index(min(numssorted, key=lambda x:abs(x-(target-min(nums)))))+1
        # numssorted = numssorted[:minelementindex]
        for a in numssorted:
            if (target - a) in numssorted[numssorted.index(a):]:
                first = nums.index(a)
                nums[first] = float('inf')
                second = nums.index(target-a)
                return [first, second]


print(Solution().twoSum([3,2,4],6))
