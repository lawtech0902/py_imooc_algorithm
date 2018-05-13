# _*_ coding: utf-8 _*_
"""
输入一个链表，从尾到头打印链表每个节点的值。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:29'
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        if not listNode:
          return res
        head = listNode
        while head:
          res.insert(0, head.val)
          head = head.next
        return res