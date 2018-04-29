# _*_ coding: utf-8 _*_
"""
给定一个字符串，找出不含有重复字符的最长子串的长度
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:00'
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i - start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s) - start)
