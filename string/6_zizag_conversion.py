# _*_ coding: utf-8 _*_
"""
输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:04'
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for ch in s:
            L[index] += ch
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step -= 1
            index += step
        return ''.join(L)
