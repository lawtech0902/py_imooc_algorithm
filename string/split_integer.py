# _*_ coding: utf-8 _*_
"""
python实现整数均分
将整数m划分为n个整数，使得到的整数之间的差值不超过1，结果按照升序排列。
例如输入55, 6，返回[9, 9, 9, 9, 9, 10]。
__author__ = 'lawtech'
__date__ = '2018/3/22 下午2:45'
"""


def split_integer(m, n):
    assert n > 0
    quotient = m // n
    remainder = m % n
    if remainder > 0:
        return [quotient] * (n - remainder) + [quotient + 1] * remainder
    elif remainder < 0:
        return [quotient - 1] * -remainder + [quotient] * (n + remainder)
    else:
        return [quotient] * n

if __name__ == '__main__':
    print(split_integer(-55,6))
