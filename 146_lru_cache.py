# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/1 下午8:11'
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.queue:
            return -1
        val = self.queue.pop(key)
        self.queue[key] = val
        return self.queue[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.queue:
            self.queue.pop(key)
        elif len(self.queue) == self.capacity:
            self.queue.popitem(last=False)
        self.queue[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
