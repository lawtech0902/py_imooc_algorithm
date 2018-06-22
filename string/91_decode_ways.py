# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""


class Solution:
    def numDecodings(self, s):
        """
        dp解决
        初始化时，dp[0] = dp[1] = 1
        当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]。
        当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]。
        当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0':
                dp.append(dp[i-1] + dp[i-2])
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp.append(dp[i-2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]
