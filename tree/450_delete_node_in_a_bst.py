# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午2:37'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.val = self.find_max(root.left).val
            root.left = self.deleteNode(root.left, root.val)
        return root

    def find_max(self, node):
        while node.right:
            node = node.right
        return node
