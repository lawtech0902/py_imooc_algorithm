# _*_ coding: utf-8 _*_
"""
验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
__author__ = 'lawtech'
__date__ = '2018/4/28 下午2:58'
"""


class Solution:
    def isNumber(self, s):
        """
        确定有穷状态自动机DFA，什么鬼东西
        :type s: str
        :rtype: bool
        """
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        EXPONENT = 5
        # 0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable = [[-1,  0,  3,  1,  2, -1],  # 0 no input or just spaces
                           [-1,  8, -1,  1,  4,  5],  # 1 input is digits
                           # 2 no digits in front just Dot
                           [-1, -1, -1,  4, -1, -1],
                           [-1, -1, -1,  1,  2, -1],  # 3 sign
                           # 4 digits and dot in front
                           [-1,  8, -1,  4, -1,  5],
                           [-1, -1,  6,  7, -1, -1],  # 5 input 'e' or 'E'
                           [-1, -1, -1,  7, -1, -1],  # 6 after 'e' input sign
                           # 7 after 'e' input digits
                           [-1,  8, -1,  7, -1, -1],
                           [-1,  8, -1, -1, -1, -1]]  # 8 after valid input input space
        state = 0
        i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputtype = SIGN
            elif s[i] in '0123456789':
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputtype = EXPONENT

            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 1 or state == 4 or state == 7 or state == 8
