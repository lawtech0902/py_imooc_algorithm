# _*_ coding: utf-8 _*_
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""
from functools import cmp_to_key


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers or len(numbers) <= 0:
            return ''
        nums = sorted([str(num) for num in numbers],
                      key=cmp_to_key(self.compare))
        return ''.join(nums)

    def compare(self, a, b):
        return [1, -1][a+b < a-b]
