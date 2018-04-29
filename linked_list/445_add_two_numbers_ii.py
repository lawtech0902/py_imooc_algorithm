# _*_ coding: utf-8 _*_
"""
输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7
__author__ = 'lawtech'
__date__ = '2018/4/29 下午4:01'
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        1. 统计两链表长度s1, s2；最终结果链表长度s = max(s1, s2) （若有进位，则为s+1）

        2. 将两链表对齐并逐节点求和，记头节点为dummy（头节点为dummy node，最高位从dummy.next开始）

        3. 初始令指针p指向头节点h，执行循环：

            令指针q = p.next，重复向其下一节点移动，直到q为空或者q.val ≠ 9

            如果q.val ＞ 9，说明p与q之间的所有节点需要进位，令p向q移动同时修改p.val

            否则，令p = q
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        s1 = self.get_size(l1)
        s2 = self.get_size(l2)
        s = max(s1, s2)
        p = dummy = ListNode(0)
        while s:
            p.next = ListNode(0)
            p = p.next
            if s <= s1:
                p.val += l1.val
                l1 = l1.next
            if s <= s2:
                p.val += l2.val
                l2 = l2.next
            s -= 1

        p = dummy
        while p:
            q = p.next
            while q and q.val == 9:
                q = q.next
            if q and q.val > 9:
                while p != q:
                    p.val += 1
                    p = p.next
                    p.val -= 10
            else:
                p = q
        return dummy if dummy.val else dummy.next

    def get_size(self, l):
        cnt = 0
        while l:
            cnt += 1
            l = l.next
        return cnt
