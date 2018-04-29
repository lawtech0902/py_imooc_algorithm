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


# TAG = object()


class Solution(object):
    def hasCycle(self, head):
        """
        快慢指针
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # def hasCycle(self, head):
    #     """
    #     标记法
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     while head:
    #         if head.val is TAG:
    #             return True
    #         head.val = TAG
    #         head = head.next
    #     return False
