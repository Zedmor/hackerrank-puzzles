"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:


Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.


>>> Solution().canJump([1])
False
>>> Solution().canJump([1])
True

>>> Solution().canJump([2,3,1,1,4])
True
>>> Solution().canJump([3,2,1,0,4])
False
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def find_paths(pointer):
            value = nums[pointer]
            for i in range(pointer + 1, min(pointer + value + 1, len(nums) + 1)):
                if i == (len(nums) - 1) or pointer == len(nums) - 1:
                    return True
                else:
                    res = find_paths(i)
                    return True if res else False

        return find_paths(0)





