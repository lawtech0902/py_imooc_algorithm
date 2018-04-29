# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午3:24'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # 分割链表
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        # 反转head2
        pre, cur = None, head2
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 比较
        while pre:
            if pre.val != head1.val:
                return False
            pre = pre.next
            head1 = head1.next
        return True
