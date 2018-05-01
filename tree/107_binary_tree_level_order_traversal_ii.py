# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/30 下午2:34'
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        levelorder then reverse
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, res = [root], []
        if not root:
            return res
        while q:
            new_q = []
            res.append([node.val for node in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                q = new_q
        return res[::-1]
