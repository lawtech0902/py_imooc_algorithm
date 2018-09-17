# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/15 下午3:08'
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_k_group(head, k):
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    cur = pre
    size = 0
    while cur.next:
        size += 1
        cur = cur.next
    while size >= k:
        cur = pre.next
        for i in range(1, k):
            t = cur.next
            cur.next = t.next
            t.next = pre.next
            pre.next = t
        pre = cur
        size -= k
    return dummy.next


def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(' '.join(res))


if __name__ == '__main__':
    node_val = list(map(int, input().split()))
    k = int(input())
    head = ListNode(node_val[0])
    p = head
    for val in node_val[1:]:
        p.next = ListNode(val)
        p = p.next
    print_linked_list(reverse_k_group(head, k))