# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 
注意事项：您可以假定该字符串只包含小写字母。
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        for ch in s:
            if cnt[ch] == 1:
                return s.index(ch)
        return -1