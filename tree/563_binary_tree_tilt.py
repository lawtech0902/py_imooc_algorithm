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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def subTreeSum(root):
            if not root:
                return 0
            l_sum = subTreeSum(root.left)
            r_sum = subTreeSum(root.right)
            self.res += abs(l_sum - r_sum)
            return root.val + l_sum + r_sum
        subTreeSum(root)
        return self.res