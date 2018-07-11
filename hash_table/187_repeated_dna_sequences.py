# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/11 上午11:56'

所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超过一次的10个字母长的序列（子串）。

示例:

输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

输出: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dct = {}
        for i in range(len(s) - 9):
            sub_str = s[i:i + 10]
            if sub_str not in dct:
                dct[sub_str] = 1
            else:
                dct[sub_str] += 1
        res = []
        for sub_str in dct:
            if dct[sub_str] > 1:
                res.append(sub_str)
        return res
