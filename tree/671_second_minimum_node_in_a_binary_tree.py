# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:36'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('inf')
        min = root.val

        def dfs(node):
            if node:
                if min < node.val < self.res:
                    self.res = node.val
                elif node.val == min:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.res if self.res < float('inf') else -1
