# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/2 上午10:49'

给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
"""

from collections import Counter


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt_s, cnt_t = Counter(s), Counter(t)
        return list((cnt_t - cnt_s).keys()).pop()
