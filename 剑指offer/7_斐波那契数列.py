# _*_ coding: utf-8 _*_
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:39'
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a
