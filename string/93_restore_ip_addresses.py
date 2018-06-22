# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'


给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        res = []
        if size < 4 or size > 12:
            return res
        for i in range(1, size-2):
            first = int(s[:i])
            if first > 255:
                break
            for j in range(i+1, size-1):
                second = int(s[i:j])
                if second > 255:
                    break
                for k in range(j+1, size):
                    third = int(s[j:k])
                    if third > 255:
                        break
                    last = s[k:]
                    if last > 255:
                        continue
                    ip = '.'.join(map(str, [first, second, third, last]))
                    if len(ip) == size + 3:
                        res.append(ip)
        return res
