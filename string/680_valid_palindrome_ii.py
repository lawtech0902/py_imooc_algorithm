# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/12 上午11:20'

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""


class Solution:
    def validPalindrome(self, s):
        """
        双指针，遇不等时去掉再判断是否是回文串
        :type s: str
        :rtype: bool
        """
        is_palindrome = lambda s: s == s[::-1]
        str_part = lambda s, x: s[:x] + s[x + 1:]
        size = len(s)
        low, high = 0, size - 1
        while low < high:
            if s[low] != s[high]:
                return is_palindrome(str_part(s, low)) or is_palindrome(str_part(s, high))
            low += 1
            high -= 1
        return True
