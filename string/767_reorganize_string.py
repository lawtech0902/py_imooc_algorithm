# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/21 上午10:49'
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。
"""

import collections


class Solution:
    def reorganizeString(self, S):
        """
        贪心：将字母按照出现次数从大到小排序。
        每次优先选择剩余次数最多，且与新字符串末尾字符串不重复的字符，排在末尾。
        若某次选择无法找出这样的字符，则返回空串。
        :type S: str
        :rtype: str
        """
        cnt = collections.Counter(S)
        res = '#'
        while cnt:
            stop = True
            for v, c in cnt.most_common():
                if v != res[-1]:
                    res += v
                    cnt[v] -= 1
                    if not cnt[v]:
                        del cnt[v]
                    stop = False
                    break
            if stop:
                break
        return res[1:] if len(res) == 1 + len(S) else ''
