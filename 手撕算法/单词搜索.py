# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/9 下午3:35'

百词斩笔试
"""


def exist(grid, word):
    def dfs(x, y, word):
        if len(word) == 0:
            return True
        # 向上
        if x > 0 and grid[x - 1][y] == word[0]:
            tmp = grid[x][y]
            grid[x][y] = '#'
            if dfs(x - 1, y, word[1:]):
                return True
            grid[x][y] = tmp
        # 向下
        if x < len(grid) - 1 and grid[x + 1][y] == word[0]:
            tmp = grid[x][y]
            grid[x][y] = '#'
            if dfs(x + 1, y, word[1:]):
                return True
            grid[x][y] = tmp
        # 向左
        if y > 0 and grid[x][y - 1] == word[0]:
            tmp = grid[x][y]
            grid[x][y] = '#'
            if dfs(x, y - 1, word[1:]):
                return True
            grid[x][y] = tmp
        # 向右
        if y < len(grid[0]) - 1 and grid[x][y + 1] == word[0]:
            tmp = grid[x][y]
            grid[x][y] = '#'
            if dfs(x, y + 1, word[1:]):
                return True
            grid[x][y] = tmp
        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0][0]:
                if dfs(i, j, word[1:]):
                    return True
    return False


if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    grid = []
    for _ in range(m):
        grid.append(list(input()))
    word = input()
    flag = exist(grid, word)
    if flag:
        print('true')
    else:
        print('false')
