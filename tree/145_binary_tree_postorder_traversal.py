# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/29 下午5:05'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
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
                    node.append(node.left)
                if node.right:
                    node.append(node.right)
        return res[::-1]

    # def postorderTraversal(self, root):
    #     """
    #     递归
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if not root:
    #         return res
    #     res.extend(self.postorderTraversal(root.left))
    #     res.extend(self.postorderTraversal(root.right))
    #     res.append(root.val)
    #     return res
