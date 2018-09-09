# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/2 下午5:22'
"""


class Solution:
    def FindGreatestSumOfSubArray(self, nums):
        max_sum = nums[0]
        pre_sum = 0
        for num in nums:
            if pre_sum < 0:
                pre_sum = num
            else:
                pre_sum += num
                max_sum = max(max_sum, pre_sum)
        return max_sum
