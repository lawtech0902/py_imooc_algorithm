# _*_ coding: utf-8 _*_
"""
一个链表中包含环，请找出该链表的环的入口结点。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, head):
        # write code here
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
