# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/5 下午2:29'

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例:

输入: [2,1,5,6,2,3]
输出: 10

解法：
以[2,1,5,6,2,3]模拟整个过程

2进栈，stack = [2]，maxArea = 0；
1比栈顶元素stack[-1]小，2出栈，maxArea = 2*1 =2；2被替换为1进栈，1继续进栈，stack = [1,1] ，maxArea =2；
5比栈顶元素stack[-1]大，5进栈，栈为stack = [1,1，5] ，maxArea =2；
6比栈顶元素stack[-1]大，6进栈，栈为stack = [1,1,5,6] ，maxArea =2；
2比栈顶元素stack[-1]小，是一个降序点；此时栈长为4，开始弹栈，6出栈，maxArea =6*1=6（当前height*1（4-数字6在栈中的下标））；接着判断，2比栈顶元素5小，5出栈maxArea =5*2=6（当前height = 5,width =4-2=2（4-数字5在栈中的下标））；下一个1比,2小，不需出栈。然后将弹出5、6的空位压栈为2，2继续入栈，stack = [1,1,2,2,2]，maxArea = 10；
3比栈顶元素2大，入栈，stack = [1,1,2,2,2,3]，maxArea = 10；
最后判断每个点作为起始点的最大面积，max(height[i]*(size-i))=max{3*1, 2*2, 2*3, 2*4, 1*5, 1*6}= 8 < 10。遍历结束。整个过程中max的area为10.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        area = 0
        while i < len(heights):
            if not stack or heights[i] > heights[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if not stack else i - stack[len(stack) - 1] - 1
                area = max(area, width * heights[curr])
                i -= 1
            i += 1
        while stack:
            curr = stack.pop()
            width = i if not stack else len(heights) - stack[len(stack) - 1] - 1
            area = max(area, width * heights[curr])
        return area

    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     res = 0
    #     size = len(heights)
    #     for i in range(size):
    #         if i + 1 < size and heights[i] < heights[i + 1]:
    #             continue
    #         min_height = heights[i]
    #         for j in range(i, -1, -1):
    #             min_height = min(min_height, heights[j])
    #             area = min_height * (i - j + 1)
    #             res = max(area, res)
    #     return res
