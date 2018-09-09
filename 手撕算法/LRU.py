# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/2 下午10:36'
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        if key in self.items:
            self.items.pop(key)
        elif len(self.items) == self.capacity:
            self.items.popitem(last=True)
        self.items[key] = value

    def __getitem__(self, key):
        val = self.items.get(key)
        if val:
            self.items.pop(key)
            self.items[key] = val
        return val

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':
    d = LRUCache(10)

    for i in range(15):
        d[i] = i
    print(d)
