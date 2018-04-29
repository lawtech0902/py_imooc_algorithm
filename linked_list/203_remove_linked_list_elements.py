# _*_ coding: utf-8 _*_
"""
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
__author__ = 'lawtech'
__date__ = '2018/4/29 下午3:12'
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
