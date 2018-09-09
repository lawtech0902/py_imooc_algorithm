# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/2 下午5:24'

先找出nums列表中出现频率最高的元素HighKey（可能有多个），然后遍历这些值，找到它们的index的最大和最小，最后比较大小，输出最小的。
"""

from collections import Counter, defaultdict


class Solution:
    def findShortestSubArray(self, nums):
        degree = max(Counter(nums).values())
        so_far = defaultdict(int)
        min_size = len(nums)
        start = 0
        for end, num in enumerate(nums):
            so_far[num] += 1
            while start <= end and so_far[num] == degree:
                min_size = min(min_size, end - start + 1)
                so_far[nums[start]] -= 1
                start += 1
        return min_size
