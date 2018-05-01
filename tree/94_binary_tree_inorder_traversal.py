# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午4:46'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        迭代
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    # def inorderTraversal(self, root):
    #     """
    #     递归
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if not root:
    #         return res
    #     res.extend(self.inorderTraversal(root.left))
    #     res.append(root.val)
    #     res.extend(self.inorderTraversal(root.right))
    #     return res
