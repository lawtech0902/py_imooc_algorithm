# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:04'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import Counter


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        if not root:
            return vals

        def dfs(node):
            if not node:
                return 0
            s = dfs(node.left) + node.val + dfs(node.right)
            vals.append(s)
            return s
        dfs(root)
        count = Counter(vals)
        max_cnt = max(count.values())
        return [k for k, v in count.items() if v == max_cnt]
