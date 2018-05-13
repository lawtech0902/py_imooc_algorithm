# _*_ coding: utf-8 _*_
"""
操作给定的二叉树，将其变换为源二叉树的镜像。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root
