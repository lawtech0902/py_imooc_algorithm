# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/5 下午7:48'


给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6


找到平面上在一条直线上最多的点。
点在同一条直线上意味着这些点的斜率是一样的，那么可以考虑使用哈希表来解决，{斜率：[点1，点2]}这样的映射关系。
这里有几个需要考虑的要点：1，有可能是斜率无穷大。2，有可能有相同的点，比如[(1,2),(1,2)]。
"""
from decimal import Decimal


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        size = len(points)
        if size < 3:
            return size
        res = -1
        for i in range(size):
            slope = {'inf': 0}
            same_points_num = 1
            for j in range(size):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = Decimal((points[i].y - points[j].y) / (points[i].x - points[j].x))
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:
                    same_points_num += 1
            res = max(res, max(slope.values()) + same_points_num)
        return res
