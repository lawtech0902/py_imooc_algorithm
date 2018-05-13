# _*_ coding: utf-8 _*_
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        candidate, cnt = None, 0
        for num in numbers:
            if cnt == 0:
                candidate = num
                cnt += 1
            elif num == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate if numbers.count(candidate) > len(numbers)//2 else 0