# _*_ coding: utf-8 _*_
"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class Solution:
    def FindNumbersWithSum(self, nums, target):
        # write code here
        if not nums or nums[-1] + nums[-2] < target:
            return []
        low, high = 0, len(nums) - 1
        while low < high:
            cur_sum = nums[low] + nums[high]
            if cur_sum < target:
                low += 1
            elif cur_sum > target:
                high -= 1
            else:
                return [nums[low], nums[high]]
        return []
