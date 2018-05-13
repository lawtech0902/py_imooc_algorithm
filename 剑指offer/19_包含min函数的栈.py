# _*_ coding: utf-8 _*_
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node < self.min():
            self.min_stack.append(node)
        else:
            tmp = self.min()
            self.min_stack.append(tmp)

    def pop(self):
        if not self.stack or not self.min_stack:
            return None
        self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
