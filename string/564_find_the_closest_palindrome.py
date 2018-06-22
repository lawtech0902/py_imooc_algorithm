# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/12 上午10:42'

给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。

“最近的”定义为两个整数差的绝对值最小。

示例 1:

输入: "123"
输出: "121"
注意:

n 是由字符串表示的正整数，其长度不超过18。
如果有多个结果，返回最小的那个。
"""


class Solution:
    def nearestPalindromic(self, n):
        """
        记n的前半部分为p，分别用p，p - 1，p + 1及其逆序串拼接成长度为奇数或者偶数的回文串。

        假设n的长度为m， p的长度应分别取m / 2，m / 2 + 1。

        另外需要考虑进位时的边界情况，比如测试用例：11, 1001, 999
        :type n: str
        :rtype: str
        """
        evenPal = lambda sp: int(sp + sp[::-1])
        oddPal = lambda sp: int(sp + sp[::-1][1:])
        sn, n = n, int(n)
        if len(sn) == 1: return str(n - 1)
        ans = -999999999999999999
        mid = len(sn) // 2
        for sp in sn[:mid], sn[:mid + 1], str(int(sn[:mid]) * 10):
            p = int(sp)
            for pal in evenPal, oddPal:
                for d in -1, 0, 1:
                    val = pal(str(p + d))
                    if val == n: continue
                    ans = min(ans, val, key=lambda x: (abs(x - n), x))
        return str(ans)
