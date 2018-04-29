# _*_ coding: utf-8 _*_
"""
root = [1, 2, 3], k = 5 
Output: [[1],[2],[3],[],[]]

root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

首先求链表长度s

利用除数和余数将整数s划分为长度之差不大于1的k个整数，参考：Python实现整数均分:split_integer.py

然后遍历链表进行拆分
__author__ = 'lawtech'
__date__ = '2018/4/29 下午4:17'
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        size = self.listLength(root)
        for p in self.splitNum(size, k):
            if not p:
                res.append(None)
                continue
            node = root
            for _ in range(p-1):
                node = node.next
            res.append(root)
            root = node.next
            node.next = None
        return res

    def splitNum(self, m, n):
        # 将整数m划分为n个整数，使得到的整数之间的差值不超过1，结果按照升序排列。
        quotient = m // n
        remainder = m % n
        if remainder > 0:
            return [quotient] * (n-remainder) + [quotient + 1] * remainder
        elif remainder < 0:
            return [quotient - 1] * -remainder + [quotient] * (n+remainder)
        else:
            return [quotient] * n

    def listLength(self, root):
        cnt = 0
        while root:
            cnt += 1
            root = root.next
        return cnt
