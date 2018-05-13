# _*_ coding: utf-8 _*_
"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, A, B):
        # write code here
        res = False
        if A and B:
            if A.val == B.val:
                res = self.helper(A, B)
            if not res:
                res = self.helper(A.left, B)
            if not res:
                res = self.helper(A.right, B)
        return res

    def helper(self, A, B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.helper(A.left, B.left) and self.helper(A.right, B.right)
