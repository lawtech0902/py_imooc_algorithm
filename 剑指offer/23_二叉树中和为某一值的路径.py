# _*_ coding: utf-8 _*_
"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, target):
        # write code here
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == target:
                return [[root.val]]
            else:
                return []
        path = self.FindPath(root.left, target-root.val) + self.FindPath(root.right, target-root.val)
        return [[root.val] + i for i in path]