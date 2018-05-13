# _*_ coding: utf-8 _*_
"""
输入一个链表，反转链表后，输出链表的所有元素。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre, cur = None, pHead
        while cur:
          tmp = cur.next
          cur.next = pre
          pre = cur
          cur = tmp
        return pre