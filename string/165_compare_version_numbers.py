# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午4:28'

比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1
示例 2:

输入: version1 = "1.0.1", version2 = "1"
输出: 1
示例 3:

输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_lst = version1.split('.')
        v2_lst = version2.split('.')
        len_1 = len(v1_lst)
        len_2 = len(v2_lst)
        max_len = max(len_1, len_2)
        for i in range(max_len):
            v1_token = 0
            if i < len_1:
                v1_token = int(v1_lst[i])
            v2_token = 0
            if i < len_2:
                v2_token = int(v2_lst[i])
            if v1_token < v2_token:
                return -1
            if v1_token > v2_token:
                return 1
        return 0
