# _*_ coding: utf-8 _*_
"""
稠密图——邻接矩阵
__author__ = 'lawtech'
__date__ = '2018/3/13 下午8:58'
"""


class DenseGraph(object):
    def __init__(self, n, directed=False):
        self.n = n  # 顶点数
        self.m = 0  # 边数
        self.directed = directed  # 是否是有向图
        self.matrix = [[0 for i in range(n)] for i in range(n)]

    def __str__(self):
        for line in self.matrix:
            print(str(line))
        return ''

    def get_number_of_vertex(self):
        return self.n

    def get_number_of_edge(self):
        return self.m

    def add_edge(self, v, w):
        if 0 <= v < self.n and 0 <= w < self.n:
            if self.has_edge(v, w):
                return
            self.matrix[v][w] = 1
            if not self.directed:
                self.matrix[w][v] = 1
            self.m += 1

    def has_edge(self, v, w):
        if 0 <= v < self.n and 0 <= w < self.n:
            return self.matrix[v][w]
        else:
            raise Exception('Vertex not in the graph')
