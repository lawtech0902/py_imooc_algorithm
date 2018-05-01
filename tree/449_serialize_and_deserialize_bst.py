# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午2:36'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def pre_order(root):
            if root:
                vals.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = build(min_val, val)
                root.right = build(val, max_val)
                return root
        return build(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
