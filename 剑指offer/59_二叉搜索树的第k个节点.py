# _*_ coding: utf-8 _*_
"""
给定一颗二叉搜索树，请找出其中的第k大的结点。
例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, root, k):
        # write code here
        if not root or not k:
            return None
        res = []

        def inorder(node):
            if len(res) >= k or not node:
                return None
            inorder(node.left)
            res.append(node)
            inorder(node.right)
        inorder(root)
        if len(res) < k:
            return None
        return res[k-1]
