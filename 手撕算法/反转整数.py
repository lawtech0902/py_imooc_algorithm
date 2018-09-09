# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/9 下午3:37'

百词斩笔试
"""


def reverse(x):
    flag = -1 if x < 0 else 1
    n = flag * int(str(abs(x))[::-1])
    return n if n.bit_length() < 32 else 0


if __name__ == '__main__':
    x = input()
    print(reverse(x))
