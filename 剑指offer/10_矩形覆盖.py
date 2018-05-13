# _*_ coding: utf-8 _*_
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:45'
"""

class Solution:
    def rectCover(self, n):
        # write code here
        if n < 2:
            return n
        dp = [1] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]