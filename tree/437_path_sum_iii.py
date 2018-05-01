# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午2:26'
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
        :rtype: int
        """
        if not root:
            return 0
        res = self.pathSumWithRoot(
            root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return res

    def pathSumWithRoot(self, root, sum):
        if not root:
            return 0
        ans = 0
        if root.val == sum:
            ans += 1
        ans += self.pathSumWithRoot(root.left, sum - root.val) + \
            self.pathSumWithRoot(root.right, sum - root.val)
        return ans
