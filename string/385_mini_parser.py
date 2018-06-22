# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
"""

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution(object):
    def deserialize(self, s):
        """
        利用栈（Stack）数据结构
        遍历字符串s，记当前字符为c
        如果c为'-'，则将符号变量negmul置为-1
        如果c为0-9，则利用变量sigma存储数字的值
        如果c为'['，则新建一个类型为列表的NestedInteger并压栈
        如果c为']'或者','：
        若sigma非空，则将sigma * negmul加入栈顶元素；
        将栈顶元素弹出记为top；若此时栈非空，将top加入栈顶元素；否则返回top
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        sigma, negmul = None, 1
        for c in s:
            if c == '-':
                negmul = -1
            elif '0' <= c <= '9':
                sigma = (sigma or 0) * 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            else:
                if sigma is not None:
                    stack[-1].add(NestedInteger(sigma * negmul))
                    sigma, negmul = None, 1
                if c == ']':
                    top = stack.pop()
                    if stack:
                        stack[-1].add(top)
                    else:
                        return top
        return NestedInteger((sigma or 0) * negmul)
