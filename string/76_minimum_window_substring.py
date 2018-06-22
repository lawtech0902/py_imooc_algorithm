# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""


class Solution:
    def minWindow(self, s, t):
        """
        双指针法，从头从尾扫描
        :type s: str
        :type t: str
        :rtype: str
        """
        count1 = {}
        count2 = {}
        for char in t:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1
        for char in t:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1
        count = len(t)
        start, min_size, min_start = 0, 100000, 0
        for end in range(len(s)):
            if s[end] in count2 and count2[s[end]] > 0:
                count1[s[end]] -= 1
                if count1[s[end]] >= 0:
                    count -= 1
            if count == 0:
                while True:
                    if s[start] in count2 and count2[s[start]] > 0:
                        if count1[s[start]] < 0:
                            count1[s[start]] += 1
                        else:
                            break
                    start += 1
                if min_size > end-start + 1:
                    min_size = end-start+1
                    min_start = start
        if min_size == 100000:
            return ''
        else:
            return s[min_start:min_start+min_size]
