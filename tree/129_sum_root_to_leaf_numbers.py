# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/30 下午8:24'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, pre_sum):
        if not root:
            return 0
        pre_sum = pre_sum * 10 + root.val
        if not root.left and not root.right:
            return pre_sum
        return self.helper(root.left, pre_sum) + self.helper(root.right, pre_sum)
