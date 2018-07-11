# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/2 上午11:35'


给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。

示例1:

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
注意:

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
"""


class Solution:
    def findWords(self, words):
        """
        集合运算
        判断输入单词的字母集合是否为键盘某一行字母集合的子集
        :type words: List[str]
        :rtype: List[str]
        """
        rs = list(map(set, ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']))
        res = []
        for word in words:
            wset = set(word.lower())
            if any(wset.issubset(rset) for rset in rs):
                res.append(word)
        return res
