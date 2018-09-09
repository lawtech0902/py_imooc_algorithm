# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/3 下午4:04'

所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超过一次的10个字母长的序列（子串）。

示例:

输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

输出: ["AAAAACCCCC", "CCCCCAAAAA"]

字典+位运算，或者进制转换。

由于直接将字符串存入字典会导致Memory Limit Exceeded，采用位操作将字符串转化为整数可以减少内存开销。
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        val_cnt = dict()
        map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        sum = 0
        for i in range(len(s)):
            sum = (sum * 4 + map[s[i]]) & 0xFFFFF
            if i < 9:
                continue
            val_cnt[sum] = val_cnt.get(sum, 0) + 1
            if val_cnt[sum] == 2:
                res.append(s[i - 9:i + 1])
        return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
