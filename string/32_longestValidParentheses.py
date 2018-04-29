# _*_ coding: utf-8 _*_
"""
最长有效括号

例：输入："（（）"
输出：2
__author__ = 'lawtech'
__date__ = '2018/4/28 下午2:49'
"""


class Solution:
    # def longestValidParentheses(self, s):
    #     """
    #     dp
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #     size = len(s)
    #     dp = [0 for _ in range(size)]
    #
    #     for i in range(1, size):
    #         if s[i] == ')':
    #             j = i - 1 - dp[i - 1]
    #             if j >= 0 and s[j] == '(':
    #                 dp[i] = dp[i - 1] + 2
    #                 if j - 1 >= 0:
    #                     dp[i] += dp[j - 1]
    #     return max(dp)

    def longestValidParentheses(self, s):
        """
        stack
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i - last)
                    else:
                        maxlen = max(maxlen, i - stack[len(stack) - 1])
        return maxlen


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses(")()())"))
