# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/1 下午11:43'
"""
import heapq
import random


class Solution:
    def findKthLargest_1(self, nums, k):
        # python偷懒方法
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_2(self, nums, k):
        # 排序 O(nlogn)
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest_3(self, nums, k):
        # O(n) quick select 空间换时间
        pivot = random.choice(nums)
        less, more = [], []
        for num in nums:
            if num > pivot:
                more.append(num)
            elif num < pivot:
                less.append(num)
        if k <= len(more):
            return self.findKthLargest_3(more, k)
        if k > len(nums) - len(less):
            return self.findKthLargest_3(less, k - (len(nums) - len(less)))
        return pivot


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest_3([3, 2, 1, 5, 6, 4], 2))
