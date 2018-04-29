# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午9:23'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        size = len(nums)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[size // 2])
        root.left = self.sortedArrayToBST(nums[:size//2])
        root.right = self.sortedArrayToBST(nums[size//2 + 1:])
        return root
