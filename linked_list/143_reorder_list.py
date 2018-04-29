# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:52'
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    
        head1 = head
        head2 = slow.next
        slow.next = None
        
        cur, pre = head2, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        cur1, cur2 = head1, pre
        while cur2:
            next1, next2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1, cur2 = next1, next2