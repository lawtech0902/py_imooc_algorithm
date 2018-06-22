# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午8:11'
"""


class Solution:
    def majorityElement(self, nums):
        """
        moore投票算法扩展
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        size = len(nums)
        return [n for n in [n1, n2] if n is not None and nums.count(n) > size / 3]
