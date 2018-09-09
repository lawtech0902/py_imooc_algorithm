# _*_ coding: utf-8 _*_
"""
并查集实现与优化
__author__ = 'lawtech'
__date__ = '2018/3/7 下午7:03'
"""


class UnionFind(object):

    def __init__(self, count=10):
        self.count = count
        self.rank = [1 for x in range(count)]
        self.parent = [x for x in range(count)]

    def find(self, p):
        if p >= 0 and p < self.count:
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p
        else:
            raise KeyError("key not in parent")

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)
        if p_root == q_root:
            return
        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1


if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(1, 3)
    uf.union(4, 5)
    uf.union(4, 6)
    uf.union(3, 6)
    print(uf.is_connected(1, 6))
