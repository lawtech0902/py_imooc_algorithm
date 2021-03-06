# _*_ coding: utf-8 _*_
"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:23'
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array or len(array) == 0 or len(array[0]) == 0:
          return False
        j = len(array[0]) - 1
        for i in range(len(array)):
          while j and array[i][j] > target:
            j -= 1
          if array[i][j] == target:
            return True
        return False