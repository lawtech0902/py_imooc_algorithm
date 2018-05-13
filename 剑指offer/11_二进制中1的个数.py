# _*_ coding: utf-8 _*_
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:49'
"""

class Solution:
    def NumberOf1(self, n):
        # write code here
        flag = 1
        count = 0
        maxBit = 32
        for _ in range(maxBit):
            if n & flag:
                count += 1
            flag = flag << 1
        return count