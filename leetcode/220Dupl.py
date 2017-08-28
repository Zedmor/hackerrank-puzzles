class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, t, k):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        inums = list(enumerate(nums))
        inums = sorted(inums, key=lambda x: x[1])
        ixsorted = [x[0] for x in inums]
        numssorted = [x[1] for x in inums]
        distances = [abs(j - i) for i, j in
                     zip(numssorted[:-1], numssorted[1:])]
        tcand = 0
        kcand = 0
        found = False
        for i, distance in enumerate(distances):
            if distance <= t and abs(ixsorted[i] - ixsorted[i + 1]) <= k:
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

nums = [1,3,6,2]
k = 2
t = 1

print(Solution().containsNearbyAlmostDuplicate(nums, k, t))