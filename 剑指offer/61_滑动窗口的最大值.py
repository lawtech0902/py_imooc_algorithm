# _*_ coding: utf-8 _*_
"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class Solution:
    def maxInWindows(self, nums, size):
        # write code here
        slip_max = []
        if not nums or size > len(nums) or not size:
            return slip_max
        for i in range(len(nums) - size + 1):
            slip_max.append(max(nums[i:i+size]))
        return slip_max
