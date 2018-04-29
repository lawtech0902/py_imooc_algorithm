# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午5:13'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        使用堆这一数据结构，首先将每条链表的头节点进入堆中，然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，最终形成的链表就是归并好的链表。
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
          if node:
            heap.append((node.val, node))
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
          pop = heapq.heappop(heap)
          cur.next = ListNode(pop[0])
          cur = cur.next
          if pop[1].next:
            heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return dummy.next


          
