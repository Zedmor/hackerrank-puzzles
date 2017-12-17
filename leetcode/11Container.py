class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = 0
        i = 0
        j = len(height) - 1
        while j > i:
            vol = max(vol, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j-=1
        return vol


s = Solution()
print(s.maxArea([9, 6, 14, 11, 2, 2, 4, 9, 3, 8]))
