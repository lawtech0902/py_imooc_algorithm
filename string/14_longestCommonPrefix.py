# _*_ coding: utf-8 _*_
"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:09'
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for str in strs[1:]:
            while str.find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if prefix == '':
                    return ''
        return prefix
