# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/1 下午5:17'
"""


class Solution:
    @staticmethod
    def in_order(root):
        # 迭代
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def in_order_recur(self, root):
        # 递归
        res = []
        if not root:
            return res
        res.extend(self.in_order_recur(root.left))
        res.append(root.val)
        res.extend(self.in_order_recur(root.right))
