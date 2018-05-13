# _*_ coding: utf-8 _*_
"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, node):
        # write code here
        if not node:
            return None
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            while node.next:
                if node == node.left.next:
                    return node.next
                node = node.next
        return None
