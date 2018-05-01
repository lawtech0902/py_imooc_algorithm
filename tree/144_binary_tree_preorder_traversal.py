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
    def preorderTraversal(self, root):
        """
        迭代
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res

    # def preorderTraversal(self, root):
    #     """
    #     递归
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if not root:
    #         return res
    #     res.append(root.val)
    #     if root.left:
    #         res.extend(self.preorderTraversal(root.left))
    #     if root.right:
    #         res.extend(self.preorderTraversal(root.right))
    #     return res
