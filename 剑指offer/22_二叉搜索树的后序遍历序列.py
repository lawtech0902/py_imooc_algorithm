# _*_ coding: utf-8 _*_
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def VerifySquenceOfBST(self, seq):
        # write code here
        size = len(seq)
        if size <= 0:
            return False
        root = seq[-1]
        if min(seq) > root or max(seq) < root:
            # 只有一个子树
            return True
        
        index = 0
        for i in range(size - 1):
            index = i
            if seq[i] > root:
                break
        
        for j in range(index + 1, size - 1):
            if seq[j] < root:
                return False
        
        left = right = True
        if index > 0:
            left = self.VerifySquenceOfBST(seq[:index])
        if index < size - 1:
            right = self.VerifySquenceOfBST(seq[index:size-1])
        return left and right