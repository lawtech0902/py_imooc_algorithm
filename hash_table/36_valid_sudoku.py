# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/25 下午6:27'

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y] == tmp: return False
            for i in range(9):
                if board[x][i] == tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp: return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                tmp = board[i][j]
                board[i][j] = 'D'
                if not isValid(i, j, tmp):
                    return False
                else:
                    board[i][j] = tmp
        return True
