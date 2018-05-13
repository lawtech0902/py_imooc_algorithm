# _*_ coding: utf-8 _*_
"""
统计一个数字在排序数组中出现的次数。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)