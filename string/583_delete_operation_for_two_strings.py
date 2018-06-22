# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/11 下午7:48'

给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
说明:

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def len_of_lcs(n1, n2, word1, word2):
            dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
            for i in range(1, n1 + 1):
                for j in range(1, n2 + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            return dp[n1][n2]

        n1, n2 = len(word1), len(word2)
        return n1 + n2 - 2 * len_of_lcs(n1, n2, word1, word2)
