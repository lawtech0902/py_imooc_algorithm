# _*_ coding: utf-8 _*_
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:33'
"""


class Solution:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, node):
        # write code here
        self.in_stack.append(node)

    def pop(self):
        # return xx
        self.move()
        return self.out_stack.pop()

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
