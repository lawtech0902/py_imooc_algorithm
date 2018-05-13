# _*_ coding: utf-8 _*_
"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:56'
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        low, high = 1, 2
        res = []
        while low < high:
            cur_sum = (high + low) * (high - low + 1) // 2
            if cur_sum == tsum:
                res.append(list(range(low, high+1)))
                low += 1
            elif cur_sum < tsum:
                high += 1
            else:
                low += 1
        return res
