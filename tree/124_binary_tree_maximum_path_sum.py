# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/30 下午8:19'
"""
import sys
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -sys.maxsize
        if not root:
            return 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        sum = root.val
        l_max, r_max = 0, 0
        if root.left:
            l_max = self.helper(root.left)
            if l_max > 0:
                sum += l_max
        if root.right:
            r_max = self.helper(root.right)
            if r_max > 0:
                sum += r_max
        self.res = max(sum, self.res)
        return max(root.val, max(root.val+l_max, root.val+r_max))
