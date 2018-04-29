# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午5:08'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1.val
                l1 = l1.next
            else:
                p.next = l2.val
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next
