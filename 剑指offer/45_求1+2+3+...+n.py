# _*_ coding: utf-8 _*_
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n+self.Sum_Solution(n-1))
