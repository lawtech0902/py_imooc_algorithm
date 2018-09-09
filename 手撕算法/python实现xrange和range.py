# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/1 下午5:03'
"""


class Solution:
    @staticmethod
    def my_range(start, stop=None, step=None):
        res = []
        s = 1  # 步长
        if step:
            s = step
        if not stop:
            start, stop = 0, start
        while True:
            if start < stop:
                res.append(start)
                start += s
            else:
                break
        return res

    @staticmethod
    def my_xrange(start, stop=None, step=None):
        s = 1
        if step:
            s = step
        if not stop:
            start, stop = 0, start
        while True:
            if start < stop:
                yield start
                start += s
            else:
                break
