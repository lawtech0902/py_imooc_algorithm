# _*_ coding: utf-8 _*_
"""
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""
import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        return heapq.nsmallest(k, tinput)
