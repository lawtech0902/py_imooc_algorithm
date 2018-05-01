# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/30 下午3:13'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, sum, [], res)
        return res

    def helper(self, root, sum, cur, res):
        if not root:
            return
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            res.append(cur + [root.val])
        if root.left:
            self.helper(root.left, sum, cur+[root.val], res)
        if root.right:
            self.helper(root.right, sum, cur+[root.val], res)
