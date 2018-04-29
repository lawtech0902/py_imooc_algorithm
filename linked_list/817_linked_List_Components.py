# _*_ coding: utf-8 _*_
"""
题目大意：
给定一个链表，头部为head，给定链表的子集G，求G的连通分量的个数。

解题思路：
Set + Two Pointers

前、后两指针pre，head遍历链表

当pre不在G中且head在G中时，令结果+1
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:48'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        gs = set(G)
        res = 0
        pre = ListNode(None)
        while head:
            if pre.val not in gs and head.val in gs:
                res += 1
                pre = head
                head = head.next
        return res
