# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/30 下午8:14'
"""

# Definition for binary tree with next pointer.


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = [root]

        def level_order(q):
            new_q = []
            if q:
                for index, node in enumerate(q):
                    node.next = q[index+1] if index+1 < len(q) else None
                    if node.left:
                        new_q.append(node.left)
                    if node.right:
                        new_q.append(node.right)
                level_order(new_q)

        level_order(q)
