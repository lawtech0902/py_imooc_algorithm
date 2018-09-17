# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/10 下午8:13'

百词斩笔试
leetcode3
"""


def len_of_longest_substring(s):
    dict, res, start = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dict:
            res = max(res, i - start)
            start = max(start, dict[ch] + 1)
        dict[ch] = i
    return max(res, len(s) - start)


if __name__ == '__main__':
    s = input()
    print(len_of_longest_substring(s))
