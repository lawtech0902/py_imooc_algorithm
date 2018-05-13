# _*_ coding: utf-8 _*_
"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:26'
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if len(s) == 0:
            return ''
        res = ''
        for ch in s:
            if ch.isspace():
                res += '%20'
            else:
                res += ch
        return res
