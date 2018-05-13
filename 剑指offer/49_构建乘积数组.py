# _*_ coding: utf-8 _*_
"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class Solution:
    def multiply(self, A):
        # write code here
        size = len(A)
        B = [1] * size
        left = 1
        for i in range(size - 1):
            left *= A[i]
            B[i+1] *= left
        right = 1
        for i in range(size - 1, 0, -1):
            right *= A[i]
            B[i-1] *= right
        return B
