# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/27 上午10:24'


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
"""


class Solution:
    def buildTrie(self, L):
        trie = {}
        t = 0
        for word in L:
            node = trie
            for letter in word:
                child = node.get(letter)
                if child is None:
                    child = {}
                    node[letter] = child
                node = child
            val = node.get('val', 0)
            if val == 0:
                t += 1
                node['num'] = t
            node['val'] = val + 1
        return (trie, t)

    def valTrie(self, string, start, size, trie):
        node = trie
        for i in range(start, start + size):
            if node.get(string[i]) is None:
                return (0, 0)  # string[start : start + size] not in trie
            node = node[string[i]]
        return (node['num'], node['val'])

    def findSubstring(self, S, L):
        lenL = len(L)
        size = len(L[0])
        trie, tt = self.buildTrie(L)
        strlen = len(S)
        arr = []
        for i in range(strlen - size + 1):
            arr.append(self.valTrie(S, i, size, trie))
        result = []
        dp = []
        for i in range(strlen - size + 1):
            wordDict = None
            wordSet = set()
            accm = 0
            if arr[i][0] > 0:
                idx = i - size * (lenL - 1)
                if i < size:
                    wordDict = {arr[i][0]: 1}
                    if arr[i][1] == 1:
                        wordSet.add(arr[i][0])
                    if len(wordSet) == tt:
                        result.append(i)
                else:
                    wordDict, wordSet, accm = dp[i - size]
                    if wordDict is None:
                        wordDict = {}
                    accm += 1
                    num = wordDict.get(arr[i][0], 0)
                    wordDict[arr[i][0]] = num + 1
                    if num + 1 >= arr[i][1]:
                        wordSet.add(arr[i][0])
                    if idx >= 0:
                        if len(wordSet) == tt:
                            result.append(idx)
                        if accm >= lenL - 1 and arr[idx][0] > 0:
                            num = wordDict.get(arr[idx][0], 0)
                            if num - 1 < arr[idx][1] and arr[idx][0] in wordSet:
                                wordSet.remove(arr[idx][0])
                            if num >= 1:
                                wordDict[arr[idx][0]] = num - 1
            dp.append((wordDict, wordSet, accm))
        return result
