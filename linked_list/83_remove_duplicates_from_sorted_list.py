# _*_ coding: utf-8 _*_
"""
输入: 1->1->2->3->3
输出: 1->2->3
__author__ = 'lawtech'
__date__ = '2018/4/28 下午7:51'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def deleteDuplicates(self, head):
    #     """
    #     递归
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head or not head.next:
    #         return head
    #     head.next = self.deleteDuplicates(head.next)
    #     return head.next if head.next and head.val == head.next.val else head

    def deleteDuplicates(self, head):
        """
        迭代
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
