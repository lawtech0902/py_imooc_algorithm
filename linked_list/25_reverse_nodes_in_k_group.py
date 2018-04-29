# _*_ coding: utf-8 _*_
"""
给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5s
__author__ = 'lawtech'
__date__ = '2018/4/28 下午7:51'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = pre
        size = 0
        while cur.next:
            size += 1
            cur = cur.next
        while size >= k:
            cur = pre.next
            for i in range(1, k):
                t = cur.next
                cur.next = t.next
                t.next = pre.next
                pre.next = t
            pre = cur
            size -= k
        return dummy.next
