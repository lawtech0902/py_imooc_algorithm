# _*_ coding: utf-8 _*_
"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
__author__ = 'lawtech'
__date__ = '2018/4/28 下午2:58'
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        len_s = len(haystack)
        len_t = len(needle)
        for i in range(len_s - len_t + 1):
            j = 0
            while j < len_t:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1

