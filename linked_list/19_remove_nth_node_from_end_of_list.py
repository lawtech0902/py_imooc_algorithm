# _*_ coding: utf-8 _*_
"""
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
__author__ = 'lawtech'
__date__ = '2018/4/28 下午5:01'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        快慢指针
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for _ in range(n):
          p1 = p1.next
        while p1.next:
          p1 = p1.next
          p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
