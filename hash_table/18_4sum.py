# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/26 下午6:46'

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size, res, dct = len(nums), set(), {}
        if size < 4:
            return []
        nums.sort()
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] + nums[j] not in dct:
                    dct[nums[i] + nums[j]] = [(i, j)]
                else:
                    dct[nums[i] + nums[j]].append((i, j))
        for i in range(size):
            for j in range(i + 1, size - 2):
                T = target - nums[i] - nums[j]
                if T in dct:
                    for k in dct[T]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]
