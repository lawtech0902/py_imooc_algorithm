# _*_ coding: utf-8 _*_
"""
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:00'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next or not x:
            return head
        p1 = head1 = ListNode(0)
        p2 = head2 = ListNode(0)
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = head2.next
        p2.next = None
        return head.next
