# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午2:23'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root)

    def helper(self, root):
        sum = 0
        if root.left:
            if not root.left.left and not root.left.right:
                sum += root.left.val
            else:
                sum += self.helper(root.left)
        if root.right:
            sum += self.helper(root.right)
        return sum
