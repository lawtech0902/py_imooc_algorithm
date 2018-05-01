# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午2:00'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        if not root:
            return self.res

        def dfs(root, path):
            if not root.left and not root.right:
                self.res.append(path)
            if root.left:
                dfs(root.left, path+'->'+str(root.left.val))
            if root.right:
                dfs(root.right, path+'->'+str(root.right.val))
        dfs(root, str(root.val))
        return self.res
