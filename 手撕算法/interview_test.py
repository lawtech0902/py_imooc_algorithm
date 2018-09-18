# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/11 下午1:07'
"""


def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] += dp[x - c]
    return dp[amount]


if __name__ == '__main__':
    coins = [1, 5, 10, 20, 50]
    amount = int(input())
    print(change(amount, coins))
