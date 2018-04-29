# _*_ coding: utf-8 _*_
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:13'
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return res
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, item, res):
        if right < left:
            return
        if left == 0 and right == 0:
            res.append(item)
        if left > 0:
            self.helper(left - 1, right, item + '(', res)
        if right > 0:
            self.helper(left, right - 1, item + ')', res)
