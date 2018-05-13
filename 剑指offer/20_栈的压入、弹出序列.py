# _*_ coding: utf-8 _*_
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        i = 0
        for v in pushV:
            stack.append(v)
            while stack and stack[-1] == popV[i]:
                stack.pop()
                i += 1
        return len(stack) == 0