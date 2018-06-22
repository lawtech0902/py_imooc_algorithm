# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

将非负整数转换为其对应的英文表示，确保输入小于 231 - 1 。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
               Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        lv3 = "Hundred"
        lv4 = "Thousand Million Billion".split()
        words, digits = [], 0
        while num:
            token, num = num % 1000, num // 1000
            word = ''
            if token > 99:
                word += lv1[token // 100] + ' ' + lv3 + ' '
                token %= 100
            if token > 19:
                word += lv2[token // 10 - 2] + ' '
                token %= 10
            if token > 0:
                word += lv1[token] + ' '
            word = word.strip()
            if word:
                word += ' ' + lv4[digits - 1] if digits else ''
                words += word,
            digits += 1
        return ' '.join(words[::-1]) or 'Zero'
