# _*_ coding: utf-8 _*_
"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
