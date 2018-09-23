# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/23 下午11:21'

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
"""

import math


class Solution:
    # def uniquePaths(self, m, n):
    #     """
    #     dp状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [[0] * n for x in range(m)]
    #     dp[0][0] = 1
    #     for i in range(m):
    #         for j in range(n):
    #             if i+1 < m:
    #                 dp[i+1][j] += dp[i][j]
    #             if j + 1 < n:
    #                 dp[i][j+1] += dp[i][j]
    #     return dp[m-1][n-1]

    def uniquePaths(self, m, n):
        """
        数学问题：其实就是机器人总共走m+n-2步，其中m-1步往下走，n-1步往右走，
        本质上就是一个组合问题，也就是从m+n-2个不同元素中每次取出m-1个元素的组合数。
        """
        if not m or not n:
            return 0
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))
