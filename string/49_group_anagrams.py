# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:18'
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            sorted_str = ''.join(sorted(word))
            dic[sorted_str] = [word] if sorted_str not in dic else dic[sorted_str] + [word]
        res = []
        for k, v in dic.items():
            res.append(v)
        return res
