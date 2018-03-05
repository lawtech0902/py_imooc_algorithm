# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/3/5 下午4:15'
"""


class MaxIndexHeap(object):
    """
    索引堆
    """

    def __init__(self):
        self.index_list = [0]
        self.items = {}
        self.current_size = 0

    def shift_up(self, i):
        current_value = self.items[self.index_list[i]]
        current_index = self.index_list[i]
        while i // 2 > 0:
            if self.items[self.index_list[i // 2]] < current_value:
                self.index_list[i] = self.index_list[i // 2]
                i = i // 2
            else:
                break
        self.index_list[i] = current_index

    def insert(self, k, value):
        self.index_list.append(k)
        self.items[k] = value
        self.current_size += 1
        self.shift_up(self.current_size)

    def shift_down(self, i):
        current_value = self.items[self.index_list[i]]
        current_index = self.index_list[i]
        while i * 2 <= self.current_size:
            mc = self.max_child(i)
            if current_value < self.items[self.index_list[mc]]:
                self.index_list[i] = self.index_list[mc]
                i = mc
            else:
                break
        self.index_list[i] = current_index

    def max_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.items[self.index_list[i * 2]] > self.items[self.index_list[i * 2 + 1]]:
                return i * 2
            else:
                return i * 2 + 1

    def del_first(self):
        retval = self.items[self.index_list[1]]
        del self.items[self.index_list[1]]
        if self.current_size == 1:
            self.current_size -= 1
            self.index_list.pop()
            return retval
        self.index_list[1] = self.index_list[self.current_size]
        self.index_list.pop()
        self.current_size -= 1
        self.shift_down(1)
        return retval

    def build_heap(self, items):
        self.items = items
        self.index_list = [0] + list(self.items.keys())
        self.current_size = len(items)
        i = self.current_size // 2
        while i > 0:
            self.shift_down(i)
            i -= 1

    def get_item(self, i):
        return self.items[i]

    def max_item_index(self):
        return self.index_list[1]

    def change(self, k, new_value):
        if k not in self.index_list:
            raise Exception("{} doesn't exist!".format(k))
        self.items[k] = new_value
        i = self.index_list.index(k)
        self.shift_down(i)
        self.shift_up(i)
        return True


if __name__ == '__main__':
    heap = MaxIndexHeap()
    items = {'John': 21, 'Lucy': 14, 'Jesscia': 17, '张三': 32, '李四': 11}
    heap.build_heap(items)
    heap.insert('Dark', 15)
    print('最高分: %s %s' % (heap.max_item_index(), heap.items[heap.max_item_index()]))
    print('Lucy多少分? %s' % heap.get_item('Lucy'))
    # 将Lucy的分数提高到50
    heap.change('Lucy', 50)
    print('最高分: %s %s' % (heap.max_item_index(), heap.items[heap.max_item_index()]))
    heap.del_first()
    print('最高分: %s %s' % (heap.max_item_index(), heap.items[heap.max_item_index()]))
