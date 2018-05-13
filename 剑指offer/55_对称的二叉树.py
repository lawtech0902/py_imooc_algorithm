# _*_ coding: utf-8 _*_
"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, root):
        # write code here
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left)
