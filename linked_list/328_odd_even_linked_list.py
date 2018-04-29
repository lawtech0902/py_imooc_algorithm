# _*_ coding: utf-8 _*_
"""
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.
__author__ = 'lawtech'
__date__ = '2018/4/29 下午3:30'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        while cur and cur.next:
            tmp = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = tmp
            pre = pre.next
            cur = cur.next
        return head
