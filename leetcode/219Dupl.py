"""
Given an array of integers and an integer k, find out
 whether there are two distinct indices i and j in the array such that
 nums[i] = nums[j] and the absolute difference between i and j is at most k.

Subscribe to see which companies asked this question.
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, t, k):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        inums = list(enumerate(nums))
        inums = sorted(inums,a key=lambda x: x[1])
        ixsorted = [x[0] for x in inums]
        numssorted = [x[1] for x in inums]
        distances = [abs(j - i) for i, j in
                     zip(numssorted[:-1], numssorted[1:])]
        tcand = 0
        kcand = 0
        found = False
        for i, distance in enumerate(distances):
            if distance <= t and abs(ixsorted[i] - ixsorted[i + 1]) <= k+1:
                found = True
        #         tcand = distance
        #         kcand = ixsorted[i] - ixsorted[i + 1]
        #     if distance <= t and ixsorted[i] - ixsorted[i + 1] < kcand:
        #         tcand = distance
        #         kcand = ixsorted[i] - ixsorted[i + 1]
        # if tcand > 0 or kcand > 0:
        #     return True
        # else:
        #     return False
        return found


nums = [-1, -1]
t = 1
k = 0
print(Solution().containsNearbyAlmostDuplicate(nums, t, k))