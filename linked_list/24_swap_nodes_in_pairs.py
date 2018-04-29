# _*_ coding: utf-8 _*_
"""
给定 1->2->3->4, 你应该返回 2->1->4->3.
__author__ = 'lawtech'
__date__ = '2018/4/28 下午7:51'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next
            tmp = node2.next
            node2.next = node1
            node1.next = tmp
            p.next = node2
            p = node1
        return dummy.next
