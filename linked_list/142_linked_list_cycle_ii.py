# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:39'
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow, fast = head.next, head.next.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow or fast
