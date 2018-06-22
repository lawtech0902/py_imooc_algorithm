# _*_ coding: utf-8 _*_
"""
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:

输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。


示例 2:

输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []

__author__ = 'lawtech'
__date__ = '2018/4/28 下午2:58'
"""


class Solution:
    def findSubstring(self, s, words):
        """
        O(nm)
        n, m, k = len(s), len(words[0]), len(words)
        暴力做法，枚举开始位置，判断之后长度m*k的子串是否由给定字符串集合组成，最坏复杂度为O(nmk)。
        对于长度为m的字符串，0与m位置开始的区别，只在于少了s[0:m]，多了s[m*k+1:(m+1)*k]，所以产生了许多
        冗余操作。我们根据开始位置0~m-1分类，扫描字符串s，使用一个滑动窗口记录当前匹配了那些字符串，当下一个
        字符串不在words中，清空窗口(任意包含该串的均不合法)，如果记录的出现次数超过了words中数量，表示需要滑动窗口，
        窗口中单词数量等于k时，更新答案。
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        hash = {}
        res = []
        if not s or not words:
            return res
        wsize = len(words[0])

        for str in words:
            if str in hash:
                hash[str] += 1
            else:
                hash[str] = 1
        for start in range(0, len(words[0])):
            slidingWindow = {}
            wCount = 0
            for i in range(start, len(s), wsize):
                word = s[i: i + wsize]
                if word in hash:
                    if word in slidingWindow:
                        slidingWindow[word] += 1
                    else:
                        slidingWindow[word] = 1
                    wCount += 1
                    while hash[word] < slidingWindow[word]:
                        pos = i - wsize * (wCount - 1)
                        removeWord = s[pos: pos + wsize]
                        # print i, removeWord
                        slidingWindow[removeWord] -= 1
                        wCount -= 1
                else:
                    slidingWindow.clear()
                    wCount = 0
                if wCount == len(words):
                    res.append(i - wsize * (wCount - 1))

        return res
