# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/10 下午8:20'


给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

算法步骤：

使用两个"指针"x和y，初始令y = 0

利用x遍历数组nums：

若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

算法简析：

y指针指向首个0元素可能存在的位置

遍历过程中，算法确保[y, x)范围内的元素均为0
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1
