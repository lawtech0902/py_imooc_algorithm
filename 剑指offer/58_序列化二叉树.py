# _*_ coding: utf-8 _*_
"""
请实现两个函数，分别用来序列化和反序列化二叉树
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # write code here
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append('#')
        vals = []
        preorder(root)
        return ' '.join(vals)

    def Deserialize(self, s):
        # write code here
        def deserialize():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = deserialize()
            node.right = deserialize()
            return node
        vals = iter(s.split(' '))
        return deserialize()
