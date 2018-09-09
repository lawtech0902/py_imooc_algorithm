# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/1 下午5:12'
"""


class Solution:
    def two_sum(self, nums, target):
        dict = {}
        for k, v in enumerate(nums):
            dict[v] = k
        for k, v in enumerate(nums):
            if target - v in dict:
                k2 = dict[target - v]
                if k2 != k:
                    return [k, k2]
