# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午1:36'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
          return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
