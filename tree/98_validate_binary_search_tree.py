# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午10:33'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.last_val = None
        self.is_BST = True
        self.validate(root)
        return self.is_BST

    def validate(self, root):
        if not root:
            return
        if self.last_val and self.last_val >= root.val:
            self.is_BST = False
            return
        self.last_val = root.val
        self.validate(root.right)
