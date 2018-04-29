# _*_ coding: utf-8 _*_
"""
最长递增子序列
__author__ = 'lawtech'
__date__ = '2018/4/26 下午9:44'
"""


class Solution(object):
    # def length_of_LIS(self, nums):
    #     """
    #     O(n2)
    #     :param nums:
    #     :return:
    #     """
    #     size = len(nums)
    #     dp = [1] * size
    #     for i in range(size):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp) if dp else 0

    def length_of_LIS(self, nums):
        """
        O(nlogn)
        :param nums:
        :return:
        """



if __name__ == '__main__':
    s = Solution()
    print(s.length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
