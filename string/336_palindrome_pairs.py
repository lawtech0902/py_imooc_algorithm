# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

给定一组独特的单词， 找出在给定列表中不同 的索引对(i, j),使得关联的两个单词，例如：words[i] + words[j]形成回文。

示例 1:
给定 words = ["bat", "tab", "cat"]
返回 [[0, 1], [1, 0]]
回文是 ["battab", "tabbat"]

示例 2:
给定 words = ["abcd", "dcba", "lls", "s", "sssll"]
返回 [[0, 1], [1, 0], [3, 2], [2, 4]]
回文是 ["dcbaabcd", "abcddcba", "slls", "llssssll"]

利用字典wmap保存单词 -> 下标的键值对

遍历单词列表words，记当前单词为word，下标为idx：

1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案

2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案

3). 将当前单词word拆分为左右两半left，right。

     3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
     
     3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
"""


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        w_map = {y: x for x, y in enumerate(words)}

        def is_palindrome(word):
            return word == word[::-1]
        res = set()
        for idx, word in enumerate(words):
            if '' in w_map and word != '' and is_palindrome(word):
                bidx = w_map['']
                res.add((bidx, idx))
                res.add((idx, bidx))
            r_word = word[::-1]
            if r_word in w_map:
                ridx = w_map[r_word]
                if idx != ridx:
                    res.add((idx, ridx))
                    res.add((ridx, idx))
            for i in range(1, len(word)):
                left, right = word[:i], word[i:]
                rleft, rright = left[::-1], right[::-1]
                if is_palindrome(left) and rright in w_map:
                    res.add((w_map[rright], idx))
                if is_palindrome(right) and rleft in w_map:
                    res.add((idx, w_map[rleft]))
        return list(res)
