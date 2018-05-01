# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午2:07'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(root):
            if not root:
                return 0, 0
            left, right = solve(root.left), solve(root.right)
            return (root.val + left[1] + right[1]), max(left) + max(right)
        return max(solve(root))
