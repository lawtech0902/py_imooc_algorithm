# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:00'
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.queue = OrderedDict()
        self.capacity = capacity

    def put(self, key, value):
        if key in self.queue:
            self.queue.pop(key)
        elif len(self.queue) == self.capacity:
            self.queue.popitem(last=False)
        self.queue[key] = value

    def get(self, key):
        if key not in self.queue:
            return -1
        val = self.queue.pop(key)
        self.queue[key] = val
        return self.queue[key]
