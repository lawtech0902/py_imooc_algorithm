# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:40'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        bfs
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        level = [root]
        while level:
          res.append(sum(n.val for n in level) / float(len(level)))
          level = [c for n in level for c in [n.left, n.right] if c]
        return res