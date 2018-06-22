# _*_ coding: utf-8 _*_
"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
__author__ = 'lawtech'
__date__ = '2018/4/28 下午2:58'
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        1、以输出是否为末行分为两类：

        l  非末行单词组

        对于非末行单词组，按照单词组单词数量可分为：

        n  单个单词

        只包含一个单词，规定其左对齐，不足指定长度以空格填充；

        n  多个单词

        包含count个单词，那么它有（count-1）个间隔，每个间隔放置一个空格；此时，求出不足指定长度需要的额外空格数目space_num，每个单词间隔填充space_num/（count-1）个空格；若不能整除，那么前space_num%(count-1)个间隔再次填充一个空格；

        l  末行单词组：

        n  只有一个单词，左对齐，不足指定长度以空格填充；

        n  若该组有count个单词，那么它有（count-1）个间隔，每个间隔放置一个空格；不足指定长度，末尾填充；
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            while i < len(words):
                newsize = len(words[i]) if size == 0 else size+len(words[i])+1
                if newsize <= maxWidth:
                    size = newsize
                else:
                    break
                i += 1
            spaceCount = maxWidth-size
            if i-begin-1 > 0 and i < len(words):
                everyCount = spaceCount//(i-begin-1)
                spaceCount %= i-begin-1
            else:
                everyCount = 0
            j = begin
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    s += ' '*(everyCount+1)
                    if spaceCount > 0 and i < len(words):
                        s += ' '
                        spaceCount -= 1
                    s += words[j]
                j += 1
            s += ' '*spaceCount
            res.append(s)
        return res
