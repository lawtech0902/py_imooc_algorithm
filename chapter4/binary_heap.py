# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/3/5 下午2:24'
"""

from random import randint
from chapter2_3.sort import quick_sort

import timeit


class MaxBinaryHeap(object):
    """
    最大二叉堆
    """

    def __init__(self, max=100000):
        self.heap_list = [0]
        self.current_size = 0
        self.maximum = max

    def shift_up(self, i):
        current_value = self.heap_list[i]
        while i // 2 > 0:
            if self.heap_list[i // 2] < current_value:
                self.heap_list[i] = self.heap_list[i // 2]
                i = i // 2
            else:
                break
        self.heap_list[i] = current_value

    def shift_down(self, i):
        current_value = self.heap_list[i]
        while i * 2 <= self.current_size:
            mc = self.max_child(i)
            if current_value < self.heap_list[mc]:
                self.heap_list[i] = self.heap_list[mc]
                i = mc
            else:
                break
        self.heap_list[i] = current_value

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.shift_up(self.current_size)
        if self.current_size > self.maximum:
            self.del_first()

    def del_first(self):
        retval = self.heap_list[1]
        if self.current_size == 1:
            self.current_size -= 1
            self.heap_list.pop()
            return retval
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.shift_down(1)
        return retval

    def max_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, alist):
        self.heap_list = [0] + alist[:]
        self.current_size = len(alist)
        i = self.current_size // 2
        while i > 0:
            self.shift_down(i)
            i -= 1
        overflow = self.current_size - self.maximum
        for i in range(overflow):
            self.del_first()

    def heap_sort(self, alist):
        self.build_heap(alist)
        sorted_list = [self.del_first() for x in range(self.current_size)]
        sorted_list.reverse()
        return sorted_list

    def heap_sort_autochthonic(self, alist):
        self.build_heap(alist)
        while self.current_size > 1:
            self.heap_list[1], self.heap_list[self.current_size] = self.heap_list[self.current_size], self.heap_list[1]
            self.current_size -= 1
            self.shift_down(1)
        return self.heap_list[1:]


class MinBinaryHeap(MaxBinaryHeap):
    """
    最小二叉堆
    """

    def __init__(self):
        super(MinBinaryHeap, self).__init__()

    def shift_up(self, i):
        current_value = self.heap_list[i]
        while i // 2 > 0:
            if self.heap_list[i // 2] > current_value:
                self.heap_list[i] = self.heap_list[i // 2]
                i // 2
            else:
                break
        self.heap_list[i] = current_value

    def shift_down(self, i):
        current_value = self.heap_list[i]
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if current_value > self.heap_list[mc]:
                self.heap_list[i] = self.heap_list[mc]
                i = mc
            else:
                break
        self.heap_list[i] = current_value

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


if __name__ == '__main__':
    heap = MaxBinaryHeap()

    # pre_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # print(heap.heap_sort_autochthonic(pre_list))

    max = 5000
    list = [randint(-max, max) for i in range(max)]
    alist = list[:]
    blist = list[:]
    clist = list[:]

    t1 = timeit.Timer('heap.heap_sort(alist)', 'from __main__ import heap, alist')
    print('堆排序：{} s'.format(t1.timeit(number=1)))

    t2 = timeit.Timer('heap.heap_sort_autochthonic(blist)', 'from __main__ import heap, blist')
    print('原地堆排序：{} s'.format(t2.timeit(number=1)))

    t3 = timeit.Timer('quick_sort(clist)', 'from __main__ import quick_sort, clist')
    print('快速排序：{} s'.format(t3.timeit(number=1)))
