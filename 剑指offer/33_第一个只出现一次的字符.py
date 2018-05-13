# _*_ coding: utf-8 _*_
"""
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        from collections import Counter
        cnt = Counter(s)
        for i in s:
            if cnt[i] == 1:
                return s.index(i)