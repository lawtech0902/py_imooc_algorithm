# _*_ coding: utf-8 _*_
"""
输入两个链表，找出它们的第一个公共结点。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1
