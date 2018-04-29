# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:03'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        迭代
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    # def reverseList(self, head):
    #     """
    #     递归
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     return self.helper(head, None)

    # def helper(self, head, newHead):
    #     if not head:
    #         return newHead
    #     tmp = head.next
    #     head.next = newHead
    #     return self.helper(tmp, head)
