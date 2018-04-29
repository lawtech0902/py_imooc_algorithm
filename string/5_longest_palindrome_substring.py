# _*_ coding: utf-8 _*_
"""
最长回文子串
__author__ = 'lawtech'
__date__ = '2018/4/26 下午9:55'
"""


class Solution(object):
    # def longestPalindrome(self, s):
    #     """
    #     中心扩展法
    #     """
    #     palindrome = ''
    #     for i in range(len(s)):
    #         len1 = len(self.getLongestPalindrome(s, i, i))
    #         if len1 > len(palindrome):
    #             palindrome = self.getLongestPalindrome(s, i, i)
    #         len2 = len(self.getLongestPalindrome(s, i, i + 1))
    #         if len2 > len(palindrome):
    #             palindrome = self.getLongestPalindrome(s, i, i + 1)
    #     return palindrome
    #
    # def getLongestPalindrome(self, s, l, r):
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #     return s[l + 1:r]

    def longestPalindrome(self, s):
        """
        manacher
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[C - (i - C)])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abcdzdcab"))
