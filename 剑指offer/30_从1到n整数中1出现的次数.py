# _*_ coding: utf-8 _*_
"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt = 0
        for item in range(1, n+1):
            pStr = str(item)
            cnt += pStr.count('1')
        return cnt