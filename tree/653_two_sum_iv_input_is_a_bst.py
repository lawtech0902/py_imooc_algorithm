# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午3:31'
"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def findTarget(self, root, k):
    #     """
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: bool
    #     """
    #     if not root:
    #         return False
    #     bfs, s = [root], set()
    #     for i in bfs:
    #         if k - i.val in s:
    #             return True
    #         s.add(i.val)
    #         if i.left:
    #             bfs.append(i.left)
    #         if i.right:
    #             bfs.append(i.right)
    #     return False
    def findTarget(self, root, k):
        """
        bfs中序有序
        """
        nums = []
        self.bfs(root, nums)
        l, r = 0, len(nums) - 1
        while l < r:
            if k == nums[l] + nums[r]:
                return True
            elif k < nums[l] + nums[r]:
                r -= 1
            else:
                l += 1
        return False

    def bfs(self, root, nums):
        if not root:
            return nums
        self.bfs(root.left, nums)
        nums.append(root.val)
        self.bfs(root.right, nums)
