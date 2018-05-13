# _*_ coding: utf-8 _*_
"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        # write code here
        q, res = [root], []
        if not root:
            return res
        while q:
            new_q = []
            res.append([node.val for node in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return res
