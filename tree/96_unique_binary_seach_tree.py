# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午5:10'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numTrees(self, n):
        """
        卡特兰树
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        if n < 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]
            for i in range(3, n+1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1] * dp[i-j]
            return dp[n]
