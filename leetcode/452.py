"""There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the
horizontal diameter. Since it's horizontal, y-coordinates don't matter and
hence the x-coordinates of start and end of the diameter suffice. Start is
always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the
x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
arrow once shot keeps travelling up infinitely. The problem is to find the
minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation: One way is to shoot one arrow for example at x = 6 (bursting the
balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
balloons). """


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        initlen = len(points)
        non_overlappers = []
        rejected = []
        if not points:
            return 0
        counter = 1
        beginindex = 0
        points.sort(key=lambda x: x[1])
        left_limit = points[beginindex][1]
        i = 1
        while i < len(points):
            if points[i][0] <= left_limit:
                rejected.append(points.pop(i))
            else:
                left_limit = points[i][1]
                rejected.append(points.pop(beginindex))
                beginindex = i-1
                # i += 1
                counter += 1
        return counter


a = Solution()
inp = [[10, 16], [2, 8], [1, 6], [7, 12]]
inp = [[1,2],[2,3],[3,4],[4,5]]

print(a.findMinArrowShots(inp))
