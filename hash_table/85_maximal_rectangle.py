# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/5 下午2:21'

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        a = [0 for _ in range(len(matrix[0]))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j] = a[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(a))
        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        i = 0
        area = 0
        while i < len(heights):
            if not stack or heights[i] > heights[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, width * heights[curr])
                i -= 1
            i += 1
        while stack:
            curr = stack.pop()
            width = i if not stack else len(heights) - stack[len(stack) - 1] - 1
            area = max(area, width * heights[curr])
        return area


if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))
