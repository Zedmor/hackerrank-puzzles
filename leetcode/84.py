class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        for index, bar in enumerate(heights):
            if not stack or bar > stack[-1]:
                stack.append(index)
            else:
                tp = stack.pop()
                areawtop = heights[tp] * 




heights = [2,1,5,6,2,3]
assert (Solution().largestRectangleArea(heights)==10)