# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/2 下午3:48'

一个链表，奇数位升序偶数位降序，让链表变成升序的。

比如：1 8 3 6 5 4 7 2 9，最后输出1 2 3 4 5 6 7 8 9。

分析：

这道题可以分成三步：

首先根据奇数位和偶数位拆分成两个链表。

然后对偶数链表进行反转。

最后将两个有序链表进行合并。
"""

from utils import ListNode


class Solution:
    def get_ascending_list(self, head):
        if not head:
            return head
        node1, node2 = self.split_list(head)
        node2 = self.reverse_list(node2)
        return self.merge_list(node1, node2)

    def split_list(self, head):
        dummy1, dummy2 = ListNode(0), ListNode(0)
        cur1, cur2 = dummy1, dummy2
        cnt = 1
        while head:
            if cnt % 2 == 1:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
            cnt += 1
        return dummy1.next, dummy2.next

    def reverse_list(self, node):
        pre, cur = None, node
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge_list(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        dummy = ListNode(0)
        p = dummy
        while node1 and node2:
            if node1.val < node2.val:
                p.next = node1
                node1 = node1.next
            else:
                p.next = node2
                node2 = node2.next
            p = p.next
        if node1:
            p.next = node1
        if node2:
            p.next = node2
        return dummy.next
