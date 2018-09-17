# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/15 下午4:07'
"""

from collections import defaultdict, deque


def divide_class(dislikes):
    graph = defaultdict(list)
    dic = {}
    for a, b in dislikes:
        graph[a].append(b)

    queue = deque([1])
    dic[1] = 0
    visited = set([1])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
                visited.add(nei)
            if nei not in dic:
                dic[nei] = dic[node] ^ 1
            else:
                if dic[nei] == dic[node]:
                    return 0
    return 1


if __name__ == '__main__':
    child_num = int(input())
    req_num = int(input())
    dislikes = []
    for _ in range(req_num):
        dislikes.append(list(map(int, input().split())))
    print(divide_class(dislikes))
