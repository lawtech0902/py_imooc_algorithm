# _*_ coding: utf-8 _*_
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:11'
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if left.index(stack.pop()) != right.index(ch):
                    return False
        return not stack
