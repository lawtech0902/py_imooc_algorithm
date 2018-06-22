# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
        若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，
        记其下标为y，交换nums[x - 1], nums[y]
        最后将nums[x]及其右边的元素就地逆置
        """
        size = len(nums)
        for x in range(size-1, -1, -1):
            if nums[x-1] < nums[x]:
                break
        if x > 0:
            for y in range(size-1, -1, -1):
                if nums[y] > nums[x-1]:
                    nums[x-1], nums[y] = nums[y], nums[x-1]
                    break
        for z in range((size - x) // 2):
            nums[x+z], nums[size-z-1] = nums[size-z-1], nums[x+z]
