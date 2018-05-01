# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午5:12'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        一般这种要求列出所有可能结果的题目都用dfs
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        """
        dfs(start, end)函数返回以start，start+1，...，end为根的二叉查找树。
        """
        if start > end:
            return [None]
        res = []
        for root_val in range(start, end+1):
            left_tree = self.dfs(start, root_val-1)
            right_tree = self.dfs(root_val+1, end)
            for i in left_tree:
                for j in right_tree:
                    root = TreeNode(root_val)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
