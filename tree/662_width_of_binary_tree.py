# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:45'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root):
        """
        二叉树层次遍历
        对二叉树节点进行标号，根节点标号为1；若某节点标号为c，则其左右孩子标号分别为2c, 2c + 1
        某层的宽度即为最右、最左节点标号之差+1
        :type root: TreeNode
        :rtype: int
        """
        q = [(root, 1)]
        res = 0
        while q:
            width = q[-1][-1] - q[0][-1] + 1
            res = max(res, width)
            new_q = []
            for node, i in q:
                if node.left:
                    new_q.append((node.left, 2 * i))
                if node.right:
                    new_q.append((node.right, 2 * i + 1))
            q = new_q
        return res
