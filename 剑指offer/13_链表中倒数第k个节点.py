# _*_ coding: utf-8 _*_
"""
输入一个链表，输出该链表中倒数第k个结点。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:54'
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
      if not head or k <= 0:
        return None
      slow = fast = head
      for _ in range(k-1):
        if not fast.next:
          return None
        fast = fast.next
      while fast.next:
        fast = fast.next
        slow = slow.next
      return slow