# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/23 下午7:46'

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = float('inf')
        res = 0
        size = len(nums)
        for i in range(size):
            left = i + 1
            right = size - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)
                if diff < min_diff:
                    min_diff = diff
                    res = total
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return res
