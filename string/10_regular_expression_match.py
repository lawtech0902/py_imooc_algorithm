# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:08'
"""

import re


class Solution:
    def isMatch(self, s, p):
        """
        懒人解法
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.match(p + '$', s) != None
