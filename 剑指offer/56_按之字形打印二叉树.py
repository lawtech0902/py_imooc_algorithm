# _*_ coding: utf-8 _*_
"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, root):
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.helper(root.left, level+1, res)
            self.helper(root.right, level+1, res)
