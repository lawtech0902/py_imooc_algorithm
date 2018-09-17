# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/14 下午8:24'
"""


def my_enumerate(seq, start=0):
    n = start
    for i in seq:
        yield n, i
        n += 1
