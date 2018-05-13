# _*_ coding: utf-8 _*_
"""
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

import sys


class Solution:
    def StrToInt(self, str):
        # write code here
        if not str:
            return 0
        strs = str.strip()
        num, flag = 0, 1
        if strs[0] == '-':
            flag = -1
            strs = strs[1:]
        elif strs[0] == '+':
            strs = strs[1:]
        for s in strs:
            if s >= '0' and s <= '9':
                num = 10 * num + ord(s) - ord('0')
            else:
                return 0
        if flag * num > sys.maxsize:
            return sys.maxsize
        if flag * num < -sys.maxsize:
            return -sys.maxsize
        return flag * num
