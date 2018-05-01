# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午1:37'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        inorder
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res == root.val
            return
        self.helper(root.right)

    # def kthSmallest(self, root, k):
    #     """
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: int
    #     """
    #     left_cnt = self.count(root.left)
    #     if left_cnt == k - 1:
    #         return root.val
    #     elif left_cnt > k - 1:
    #         return self.kthSmallest(root.left, k)
    #     return self.kthSmallest(root.right, k-left_cnt-1)

    # def count(self, node):
    #     if not node:
    #         return 0
    #     return 1 + self.count(node.left) + self.count(node.right)
