# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:
"""


class Solution:
    # def repeatedSubstringPattern(self, s):
    #     """
    #     先提取字符串的一半，然后乘以2，看生成串和原串是否相同，相同则true，
    #     否则提取字符串三分之一，然后乘以3，以此类推。
    #     :type s: str
    #     :rtype: bool
    #     """
    #     if not s or len(s) < 2:
    #         return False
    #     size = len(s)
    #     pos = size // 2
    #     while pos > 0:
    #         if size % pos == 0:
    #             sub_str = s[:pos]
    #             multiplier = size // pos
    #             if sub_str * multiplier == s:
    #                 return True
    #         pos -= 1
    #     return False

    def repeatedSubstringPattern(self, s):
        """
        大神方法：
        输入字符串的第一个字符串是重复子字符串的第一个字符
        输入字符串的最后一个字符串是重复子字符串的最后一个字符
        令S1 = S + S（其中输入字符串中的S）
        删除S1的第一个和最后一个字符，生成字符串S2。
        如果S存在于S2中，则返回true否则为false。
        """
        if not s:
            return False
        s1 = (s * 2)[1:-1]
        return s1.find(s) != -1
