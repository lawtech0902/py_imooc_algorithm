# _*_ coding: utf-8 _*_
"""
leetcode 148
单链表排序O(nlogn), 不考虑递归栈空间的情况空间O(1)
快排(不能AC)
归并
__author__ = 'lawtech'
__date__ = '2018/4/29 下午3:04'
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        归并
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 寻找中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        # 归并
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head

    def merge(self, head1, head2):
        if not head1:
          return head2
        if not head2:
          return head1
        dummy = ListNode(0)
        p = dummy
        while head1 and head2:
          if head1.val < head2.val:
            p.next = head1
            head1 = head1.next
          else:
            p.next = head2
            head2 = head2.next
          p = p.next
        if head1:
          p.next = head1
        if head2:
          p.next = head2
        return dummy.next