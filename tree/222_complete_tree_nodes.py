# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午1:31'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        如果极左子树高度==极右子树高度，则为满二叉树，否则递归计算左右子树节点数
        :type root: TreeNode
        :rtype: int
        """
        if not root:
          return 0
        hl = hr = 0
        l = r = root
        while l:
          hl += 1
          l = l.left
        while r:
          hr += 1
          r = r.right
        if hl == hr:
          return 2 ** hl - 1
        else:
          return 1 + self.countNodes(root.left) + self.countNodes(root.right)
