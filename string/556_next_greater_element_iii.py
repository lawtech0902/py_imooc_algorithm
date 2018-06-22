# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。

示例 1:

输入: 12
输出: 21
示例 2:

输入: 21
输出: -1
"""

class Solution:
    def nextGreaterElement(self, n):
        """
        参考31_next_permutation的解法
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        size = len(nums)
        for x in range(size-1, -1, -1):
          if nums[x-1] < nums[x]:
            break
        if x > 0:
          for y in range(size-1, -1, -1):
            if nums[y] > nums[x-1]:
              nums[x-1], nums[y] = nums[y], nums[x-1]
              break
        for z in range((size-x) // 2):
          nums[x+z], nums[size-z-1] = nums[size-z-1], nums[x+z]
        res = int(''.join(nums))
        return n < res < 0x7FFFFFFF and res or -1