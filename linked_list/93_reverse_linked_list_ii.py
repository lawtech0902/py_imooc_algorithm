# _*_ coding: utf-8 _*_
"""
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:09'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        q = head
        for _ in range(m-1):
            q = q.next
            p = p.next
        start = None
        end = q
        for _ in range(m, n+1):
            tmp = q.next
            q.next = start
            start = q
            q = tmp
        p.next = start
        end.next = tmp
        return dummy.next
