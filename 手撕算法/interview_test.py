# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/11 下午1:07'
"""


def bubble_sort(nums):
    exchange = False
    for i in range(len(nums) - 1 , -1, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]