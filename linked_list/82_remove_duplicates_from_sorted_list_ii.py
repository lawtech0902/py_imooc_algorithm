# _*_ coding: utf-8 _*_
"""
输入: 1->1->1->2->3
输出: 2->3
__author__ = 'lawtech'
__date__ = '2018/4/28 下午7:51'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = pre.next
        while pre.next:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if cur == pre.next:
                pre = pre.next
                cur = pre.next
            else:
                pre.next = cur.next
        return dummy.next
