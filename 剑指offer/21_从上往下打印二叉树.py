# _*_ coding: utf-8 _*_
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        q, res = [root], []
        if not root:
            return res
        while q:
            new_q = []
            res.extend(v.val for v in q)
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return res
