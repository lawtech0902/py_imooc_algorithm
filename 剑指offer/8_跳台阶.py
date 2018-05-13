# _*_ coding: utf-8 _*_
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:39'
"""


class Solution:
    def jumpFloor(self, n):
        # write code here
        if n == 1:
          return 1
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
          dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
