# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/23 下午10:57'


给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up = 0
        left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        direct = 0  # 0: go right   1: go down  2: go left  3: go up
        count = 0
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if direct == 1:
                for i in range(up, down + 1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if direct == 2:
                for i in range(right, left - 1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in range(down, up - 1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n * n:
                return matrix
            direct = (direct + 1) % 4
