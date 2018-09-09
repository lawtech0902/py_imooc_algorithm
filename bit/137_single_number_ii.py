# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/3 上午12:23'

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

使用二进制模拟三进制。在连续来3个1后清0。
使用两个bit位，bit1和bit2。
初始状态bit1和bit2都是0，即00，在来了第一个1后，变成了01，来了第二个1后变成了10，来了第三个1后，变成了11，然后清0为00，
即：00->01->10->11，然后将11清为00，这个过程就是我们编程的思路。
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0, 0, 0
        for num in nums:
            two = two | (one & num)  # two为1时，不管A[i]为什么，two都为1
            one = num ^ one  # 异或操作，都是1就进位
            three = ~(one & two)  # 以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            one &= three
            two &= three
        return one


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2]))
