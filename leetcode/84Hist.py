class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # print(heights)
        rectangles = []
        curhight = 0
        for value in heights:
            if value > curhight:
                curhight = value




a = Solution()
print(a.largestRectangleArea([2,1,5,6,2,3]))

2,1
1,1
1,2

1,3
5,1
1.4
5,2

6,1

5,2

2,1
3,2
1,5
2,2