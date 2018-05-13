# _*_ coding: utf-8 _*_
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        num_row = len(matrix)
        num_col = len(matrix[0])
        new_mat = []
        for i in range(num_col):
            new_mat2 = []
            for j in range(num_row):
                new_mat2.append(matrix[j][i])
            new_mat.append(new_mat2)
        new_mat.reverse()
        return new_mat