# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:16'
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                dfs(num + 1, string + letter, res)

        dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        if not digits:
            return res
        length = len(digits)
        dfs(0, '', res)
        return res
