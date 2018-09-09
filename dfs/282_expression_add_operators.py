# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/8/24 下午7:26'

给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"]
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []

DFS（深度优先搜索）

将字符串拆解成left + operator + right的形式，针对left执行递归

注意：包含前导0的运算数是无效的。

例如，通过"00+9"获得目标值9是不正确的。
"""

class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        return self.solve(num, target)

    def is_leading_zeros(self, num):
        return num.startswith('00') or int(num) and num.startswith('0')

    def solve(self, num, target, mul_expr="", mul_val=1):
        res = []

        # remove leading zeros
        if self.is_leading_zeros(num):
            pass
        elif int(num) * mul_val == target:
            res += num + mul_expr

        for i in range(len(num) - 1):
            lnum, rnum = num[:i + 1], num[i + 1:]
            # remove leading zeros
            if self.is_leading_zeros(rnum):
                continue
            right, rightVal = rnum + mul_expr, int(rnum) * mul_val
            # op = '+'
            for left in self.solve(lnum, target - rightVal):
                res += left + '+' + right
            # op = '-'
            for left in self.solve(lnum, target + rightVal):
                res += left + '-' + right
            # op = '*'
            for left in self.solve(lnum, target, '*' + right, rightVal):
                res += left
        return res
