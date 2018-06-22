# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/23 下午4:14'


给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

用动态规划来解决。
状态转移方程是这样的：dp[i][j]表示word1[0...i-1]到word2[0...j-1]的编辑距离。
而dp[i][0]显然等于i，因为只需要做i次删除操作就可以了。
同理dp[0][i]也是如此，等于i，因为只需做i次插入操作就可以了。
dp[i-1][j]变到dp[i][j]需要加1，因为word1[0...i-2]到word2[0...j-1]的距离是dp[i-1][j]，
而word1[0...i-1]到word1[0...i-2]需要执行一次删除，所以dp[i][j]=dp[i-1][j]+1；
同理dp[i][j]=dp[i][j-1]+1，因为还需要加一次word2的插入操作。
如果word[i-1]==word[j-1]，则dp[i][j]=dp[i-1][j-1]，
如果word[i-1]!=word[j-1]，那么需要执行一次替换replace操作，
所以dp[i][j]=dp[i-1][j-1]+1，以上就是状态转移方程的推导。
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = i
        for i in range(m):
            dp[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1]
                               [j-1]+(0 if word1[i-1] == word2[j-1] else 1))
        return dp[m-1][n-1]
