# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/15 下午8:10'
"""


def max_heapify(heap, heap_size, root):
    # 在堆中做结构调整使得父节点的值大于子节点(自堆顶向下调整)
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < heap_size and heap[larger] < heap[left]:
        larger = left
    if right < heap_size and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, heap_size, larger)


def build_max_heap(heap):
    # 构造一个堆，将堆中所有数据重新排序
    heap_size = len(heap)
    for i in range((heap_size - 2) // 2, -1, -1):
        max_heapify(heap, heap_size, i)


def heap_sort(heap):
    # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap


if __name__ == '__main__':
    test_list = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(test_list)
    heap_sort(test_list)
    print(test_list)
