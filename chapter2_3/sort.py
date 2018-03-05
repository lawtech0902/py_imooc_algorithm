# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/2/26 下午5:54'
"""

from random import *
import timeit


def selection_sort(alist):
    """
    选择排序
    :param alist:
    :return:
    """
    for i in range(0, len(alist)):
        min_index = i
        for j in range(i, len(alist), 1):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


def insertion_sort(alist):
    """
    一般版本，每次把当前的数往前插入
    :param alist:
    :return:
    """
    for i in range(1, len(alist)):
        j = i - 1
        key = alist[i]
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key
    return alist


def binary_insertion_sort(alist):
    """
    折半插入排序，在直接插入排序的基础上使用了二分查找的方法
    :param alist:
    :return:
    """
    for i in range(1, len(alist)):
        index = alist[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if index > alist[mid]:
                low = mid + 1
            else:
                high = mid - 1
        for j in range(i, low, -1):
            alist[j] = alist[j - 1]
        alist[low] = index
    return alist


def shell_sort(alist):
    """
    希尔排序
    :param alist:
    :return:
    """
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


def bubble_sort(alist):
    """
    冒泡排序
    :param alist:
    :return:
    """
    exchange = False
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist


def merge_list(a, b):
    """
    合并两个有序列表
    :param a:
    :param b:
    :return:
    """
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


def merge_sort(alist):
    """
    归并排序
    :param alist:
    :return:
    """
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return merge_list(left, right)


def quick_sort(alist):
    """
    快速排序
    :param alist:
    :return:
    """
    less = []
    pivot_list = []
    more = []
    if len(alist) <= 1:
        return alist
    elif len(alist) <= 16:  # 规模较小时使用插入排序
        insertion_sort(alist)
    pivot = choice(alist)  # 随机取基准数，解决近乎有序的列表
    for i in alist:
        # 三路快排，解决有大量重复值的列表
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            pivot_list.append(i)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivot_list + more


# alist = [10, 9, 8, 7, 6, 5, chapter4, 3, 2, 1]
# print(bubble_sort(alist))
if __name__ == '__main__':
    max = 5000
    list = [randint(-max, max) for x in range(max)]

    alist = list[:]
    blist = list[:]
    clist = list[:]
    dlist = list[:]
    elist = list[:]
    flist = list[:]
    glist = list[:]

    t1 = timeit.Timer('selection_sort(alist)', 'from __main__ import selection_sort, alist')
    print('选择排序：{} s'.format(t1.timeit(number=1)))

    t2 = timeit.Timer('insertion_sort(blist)', 'from __main__ import insertion_sort, blist')
    print('直接插入排序：{} s'.format(t2.timeit(number=1)))

    t3 = timeit.Timer('binary_insertion_sort(clist)', 'from __main__ import binary_insertion_sort, clist')
    print('折半插入排序：{} s'.format(t3.timeit(number=1)))

    t4 = timeit.Timer('shell_sort(dlist)', 'from __main__ import shell_sort, dlist')
    print('希尔排序：{} s'.format(t4.timeit(number=1)))

    t5 = timeit.Timer('bubble_sort(elist)', 'from __main__ import bubble_sort, elist')
    print('冒泡排序：{} s'.format(t5.timeit(number=1)))

    t6 = timeit.Timer('merge_sort(flist)', 'from __main__ import merge_sort, flist')
    print('归并排序：{} s'.format(t6.timeit(number=1)))

    t7 = timeit.Timer('quick_sort(glist)', 'from __main__ import quick_sort, glist')
    print('快速排序：{} s'.format(t7.timeit(number=1)))
