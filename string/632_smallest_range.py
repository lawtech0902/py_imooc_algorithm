# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/14 上午11:56'

你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1:

输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
注意:

给定的列表可能包含重复元素，所以在这里升序表示 >= 。
1 <= k <= 3500
-105 <= 元素的值 <= 105
"""

import collections


class Solution:
    def smallestRange(self, nums):
        """
        字典dmap维护映射num -> set(idx)，记录num在哪些列表（编号0~len(nums)）中出现过

        字典cover维护映射idx -> set(num)，记录当前窗口覆盖了哪些列表，以及这些列表中包含的数字

        snum为nums去重和排序的结果

        初始令窗口范围start = end = 0

        重复以下过程，直到start == len(snum) 或者end == len(snum)为止

          令end向右滑动，直到cover中包含所有列表为止

          令start向右滑动，直到cover中不再包含所有列表为止，并更新最小间隔和答案
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        dmap = collections.defaultdict(set)
        cover = collections.defaultdict(set)
        nsize = len(nums)

        for idx, nlist in enumerate(nums):
            for num in nlist:
                dmap[num].add(idx)
        snum = sorted(set(n for nlist in nums for n in nlist))
        ssize = len(snum)

        start = end = 0
        ans = [snum[0], snum[-1]]
        gap = 0x7FFFFFFF
        while start < ssize and end < ssize:
            while end < ssize and len(cover) < nsize:
                for idx in dmap[snum[end]]:
                    cover[idx].add(snum[end])
                end += 1
            while start < ssize and len(cover) == nsize:
                if len(cover) == nsize and snum[end - 1] - snum[start] < gap:
                    gap = snum[end - 1] - snum[start]
                    ans = [snum[start], snum[end - 1]]
                for idx in dmap[snum[start]]:
                    cover[idx].remove(snum[start])
                    if not cover[idx]: del cover[idx]
                start += 1
        return ans
