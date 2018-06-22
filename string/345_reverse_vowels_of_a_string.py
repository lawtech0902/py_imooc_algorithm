# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

请编写一个函数，其功能是将输入的字符串反转过来。

示例：

输入：s = "hello"
返回："olleh"
"""


class Solution:
    def reverseVowels(self, s):
        """
        双指针法
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while s[i] not in vowels and i < j:
                i += 1
            while s[j] not in vowels and i < j:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
