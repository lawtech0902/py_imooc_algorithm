# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/8/31 下午10:25'
"""


class Solution:
    def sorted_insert(self, head, node):
        cur = head
        if not cur:
            node.next = node
            head = node
            return head
        elif cur.val >= node.val:
            # 如果新节点值小于头节点值，则需要调整尾节点的后向指针
            while cur.next != head:
                cur = cur.next
            cur.next = node
            node.next = head
            head = node
        else:
            while cur.next != head and cur.next.data < node.data:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        return head
