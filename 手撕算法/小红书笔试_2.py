# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/15 下午3:23'
"""


def trailing_zeroes(n):
    return 0 if n == 0 else (n // 5 + trailing_zeroes(n // 5))


def dp_zeroes(n):
    dp = [0] * (n + 1)
    if n <= 4:
        return 0
    elif n == 5:
        return 1
    else:
        dp[5] = trailing_zeroes(5)
        for i in range(6, n + 1):
            dp[i] = trailing_zeroes(i) + dp[i - 1]
        return dp[n]


if __name__ == '__main__':
    num = int(input())
    print(dp_zeroes(num))
