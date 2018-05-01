# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:28'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        res = str(t.val)
        if t.left or t.right:
            res += '({})'.format(self.tree2str(t.left))
        if t.right:
            res += '({})'.format(self.tree2str(t.right))
        return res
