# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/2 下午2:19'

给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
"""

import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        字符统计，单词的字谜变换（anagram）是指与其字母个数相同只是顺序不同的单词
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls, lp = len(s), len(p)
        cnt_p = collections.Counter(p)
        cnt_s = collections.Counter()
        res = []
        for i in range(ls):
            cnt_s[s[i]] += 1
            if i >= lp:
                cnt_s[s[i - lp]] -= 1
                if cnt_s[s[i - lp]] == 0:
                    del cnt_s[s[i - lp]]
            if cnt_s == cnt_p:
                res.append(i - lp + 1)
        return res
