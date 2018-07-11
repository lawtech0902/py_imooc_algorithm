# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/29 下午6:19'

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深度拷贝。
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
