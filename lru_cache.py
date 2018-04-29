# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/23 上午10:36'
"""

from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = OrderedDict()

    def get(self, key):
        if key not in self.queue:
            return -1
        val = self.queue.pop(key)
        self.queue[key] = val
        return self.queue[key]

    def put(self, key, val):
        if key in self.queue:
            self.queue.pop(key)
        elif len(self.queue) == self.capacity:
            self.queue.popitem(last=False)
        self.queue[key] = val
