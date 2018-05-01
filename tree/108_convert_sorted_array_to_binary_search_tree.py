# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/30 下午2:40'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, l, r):
        if l >= r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, l, mid)
        root.right = self.helper(nums, mid+1, r)
        return root
