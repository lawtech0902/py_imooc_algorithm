# _*_ coding: utf-8 _*_
"""
最长公共子序列
__author__ = 'lawtech'
__date__ = '2018/4/26 下午9:29'
"""


class Solution(object):
    def length_of_LCS(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[l1][l2]


if __name__ == '__main__':
    s = Solution()
    print(s.length_of_LCS('abcde', 'cbacde'))
