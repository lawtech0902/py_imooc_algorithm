# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。


示例 1：

输入: ["23:59","00:00"]
输出: 1

备注:

列表中时间数在 2~20000 之间。
每个时间取值在 00:00~23:59 之间。
"""


class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))