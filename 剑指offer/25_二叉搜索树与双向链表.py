# _*_ coding: utf-8 _*_
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, root):
        # write code here
        if not root or (not root.left and not root.right):
            return root

        # 处理左子树
        self.Convert(root.left)
        left =root.left

        # 连接root与左子树最大节点
        if left:
          while left.right:
            left = left.right
          root.left, left.right = left, root
        
        # 处理右子树
        self.Convert(root.right)
        right = root.right
        
        # 连接root与右子树最小节点
        if right:
            while right.left:
                right = right.left
            root.right, right.left = right, root

        while root.left:
          root = root.left

        return root