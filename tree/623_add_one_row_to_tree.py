# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:30'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n

        q = [root]
        for i in range(1, d-1):
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q

        for node in q:
            l, r = node.left, node.right
            new_l, new_r = TreeNode(v), TreeNode(v)
            node.left, node.right = new_l, new_r
            node.left.left, node.right.right = l, r
        return root
