# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/3/6 下午1:31'
"""


def binary_search(alist, item):
    """
    非递归
    :param alist:
    :param item:
    :return:
    """
    low = 0
    high = len(alist) - 1
    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search_recursion(alist, item):
    """
    递归
    :param alist:
    :param item:
    :return:
    """
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binary_search_recursion(alist[mid + 1:], item)
        else:
            return binary_search_recursion(alist[:mid], item)


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search_recursion(alist, 3))
