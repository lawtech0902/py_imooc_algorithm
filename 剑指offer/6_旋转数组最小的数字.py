# _*_ coding: utf-8 _*_
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
__author__ = 'lawtech'
__date__ = '2018/5/9 下午9:35'
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        size = len(rotateArray)
        if size == 0:
          return 0
        low, high = 0, size - 1
        while rotateArray[low] >= rotateArray[high]:
          if high - low == 1:
            return rotateArray[high]
          mid = low + (high - low) // 2
          if rotateArray[mid] >= rotateArray[low]:
                low = mid
          else:
              high = mid
        return rotateArray[low]
