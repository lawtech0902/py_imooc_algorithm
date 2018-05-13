# _*_ coding: utf-8 _*_
"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""
from functools import reduce


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, nums):
        # write code here
        xor = reduce(lambda x, y: x ^ y, nums)
        low_bit = xor & -xor
        a, b = 0, 0
        for num in nums:
            if num & low_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]
