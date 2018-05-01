# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:54'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def traverse(node, val):
            if not node:
                return 0
            l, r = traverse(node.left, node.val), traverse(
                node.right, node.val)
            self.res = max(self.res, l+r)
            return 1 + max(l, r) if node.val == val else 0

        traverse(root, None)
        return self.res
