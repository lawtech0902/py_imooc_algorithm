# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午7:51'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        size = 0
        while p.next:
            p = p.next
            size += 1
        p.next = dummy.next
        step = size - (k % size)
        for _ in range(step):
            p = p.next
        head = p.next
        p.next = None
        return head
