# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:28'
"""

# Definition for singly-linked list with a random pointer.


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        self.copyNodes(head)
        self.connectRandomNodes(head)
        return self.reconnectRandomNodes(head)

    def copyNodes(self, head):
        node = head
        while node:
            cloned = RandomListNode(0)
            cloned.label = node.label
            cloned.next = node.next
            node.next = cloned
            node = cloned.next

    def connectRandomNodes(self, head):
        node = head
        while node:
            cloned = node.next
            if node.random:
                cloned.random = node.random.next
            node = cloned.next

    def reconnectRandomNodes(self, head):
        node = head
        clonedHead = clonedNode = node.next
        node.next = clonedHead.next
        node = node.next

        while node:
            clonedNode.next = node.next
            clonedNode = clonedNode.next
            node.next = clonedNode.next
            node = node.next

        return clonedHead
