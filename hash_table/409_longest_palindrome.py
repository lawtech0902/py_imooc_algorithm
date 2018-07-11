# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/2 上午11:11'

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""

from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        统计每个字母的出现次数：若字母出现偶数次，则直接累加至最终结果；若字母出现奇数次，则将其值-1之后累加至最终结果；
        若存在出现奇数次的字母，将最终结果+1
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        odd, res = 0, 0
        for c in cnt:
            res += cnt[c]
            if cnt[c] % 2 == 1:
                res -= 1
                odd += 1
        return res + (odd > 0)
