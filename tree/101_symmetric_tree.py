# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午10:53'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricChild(root.left, root.right)
    
    def isSymmetricChild(self, t1, t2):
        if not t1 and not t2:   return True
        if not t1 or not t2:    return False
        if t1.val != t2.val:    return False
        return self.isSymmetricChild(t1.left, t2.right) and self.isSymmetricChild(t1.right, t2.left)
