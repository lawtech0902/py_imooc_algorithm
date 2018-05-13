# _*_ coding: utf-8 _*_
"""
标准快排
__author__ = 'lawtech'
__date__ = '2018/4/24 下午8:03'
"""


def standard_quick_sort(alist, low, high):
    if low < high:
        pivot_index = partion(alist, low, high)
        standard_quick_sort(alist, low, pivot_index)
        standard_quick_sort(alist, pivot_index + 1, high)
    return alist


def partion(alist, low, high):
    pivot = alist[low]
    while low < high:
        while low < high and alist[high] >= pivot:
            high -= 1
        if low < high:
            alist[low] = alist[high]
        while low < high and alist[low] < pivot:
            low += 1
        if low < high:
            alist[high] = alist[low]
    alist[low] = pivot
    return low


if __name__ == '__main__':
    alist = [5, 4, 3, 1, 2]
    print(standard_quick_sort(alist, 0, len(alist) - 1))
