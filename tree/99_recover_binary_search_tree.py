# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午10:36'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        O(1) space, 利用prev指针来比较中序遍历中相邻的两个值
        如果利用中序有序特点进行排序重组的话，需要O(n) space
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = self.pre = None
        self.findTwoNodes(root)
        self.n1, self.n2 = self.n2, self.n1

    def findTwoNodes(self, root):
        # 利用中序有序找到两个错误位置的节点
        if root:
            self.findTwoNodes(root.left)
            if self.pre and self.pre.val >= root.val:
                self.n2 = root
                if not self.n1:
                    self.n1 = self.pre
            self.pre = root
            self.findTwoNodes(root.right)
