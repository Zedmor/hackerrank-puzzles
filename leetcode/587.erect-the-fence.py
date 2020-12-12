#
# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#
# https://leetcode.com/problems/erect-the-fence/description/
#
# algorithms
# Hard (34.54%)
# Total Accepted:    8.1K
# Total Submissions: 23.2K
# Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
#
# There are some trees, where each tree is represented by (x,y) coordinate in a
# two-dimensional garden. Your job is to fence the entire garden using the
# minimum length of rope as it is expensive. The garden is well fenced only if
# all the trees are enclosed. Your task is to help find the coordinates of
# trees which are exactly located on the fence perimeter.
#
#
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
#
#
#
# Example 2:
#
#
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
#
# Even you only have trees in a line, you need to use rope to enclose
# them.
#
#
#
#
# Note:
#
#
# All trees should be enclosed together. You cannot cut the rope to enclose
# trees that will separate them in more than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.
# input types have been changed on April 15, 2019. Please reset to default code
# definition to get new method signature.
#
#
#
"""
# >>> Solution().outerTrees([[3,7],[6,8],[7,8],[11,10],[4,3],[8,5],[7,13],[4,13]])
# [[1,1],[2,0],[4,2],[3,3],[2,4]]

# >>> Solution().outerTrees([[1,1],[2,2],[2,0],[3,3],[2,4],[4,2]])
# [[1,1],[2,0],[4,2],[3,3],[2,4]]

>>> Solution().outerTrees([[1,2],[2,2],[4,2]])
[[1,2],[2,2],[4,2]]


"""
from collections import namedtuple
from functools import partial
from math import sqrt

import matplotlib.pyplot as plt

Point = namedtuple('Point', 'x y')


def closest_distance(point, another_point):
    return sqrt((point.x - another_point.x) ** 2 + (point.y - another_point.y) ** 2)


class ConvexHull(object):
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(Point(*point))

    def _get_orientation(self, origin, p1, p2):
        '''
        Returns the orientation of the Point p1 with regards to Point p2 using origin.
        Negative if p1 is clockwise of p2.
        :param p1:
        :param p2:
        :return: integer
        '''
        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def compute_hull(self):
        '''
        Computes the points that make up the convex hull.
        :return:
        '''
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            points = sorted(points, key=partial(closest_distance, point))

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0 or (direction == 0 and far_point not in self._hull_points):
                        far_point = p2


            self._hull_points.append(far_point)
            self.display()
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)

        plt.title('Convex Hull')
        plt.show()


class Solution:
    def outerTrees(self, points: list):
        ch = ConvexHull()
        for p in points:
            ch.add(p)

        ch.compute_hull()

        ch.display()

        res = list(set([tuple(t) for t in ch.get_hull_points()]))
        res = [list(t) for t in res]

        return res



