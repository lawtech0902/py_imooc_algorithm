# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/3/6 下午2:13'
"""

import queue


class TreeNode(object):
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left_child = left
        self.right_child = right

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_chid == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_child(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left_child = lc
        self.right_child = rc

        if self.has_left_child():
            self.left_child = self

        if self.has_right_child():
            self.right_child = self

    def splice_out(self):
        """
        删除节点自身
        :return:
        """
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_chid = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_chid = self.left_child
                else:
                    self.parent.right_child = self.right_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        """
        寻找后继：选择以右孩子为根节点的子树中的最小值
        :return:
        """
        current = self.right_child
        while current.has_left_child():
            current = current.left_child
        return current

    def find_predecessor(self):
        """
        寻找前驱
        :return:
        """
        current = self.left_child
        while current.has_right_child():
            current = current.right_child
        return current


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, key, value):
        """
        插入
        :param key:
        :param value:
        :return:
        """
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._insert(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        elif key == current_node.key:
            current_node.value = value
        else:
            if current_node.has_right_child():
                self._insert(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def get(self, key):
        """
        查找
        :param key:
        :return:
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, this key is not in the tree!")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, this key is not in the tree!")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        """
        delete方法的辅助方法
        :param current_node:
        :return:
        """
        if current_node.is_leaf():
            # 第一种情况：要删除的节点是叶子节点
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            # 第二种情况：要删除的节点有两个孩子节点
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.value = succ.value
        else:
            # 第三种情况：要删除的节点只有一个孩子节点
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.value,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.value,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def get_floor_and_ceil(self, key):
        return self._get_floor_and_ceil(self.root, key, None, None)

    def _get_floor_and_ceil(self, current_node, key, floor, ceil):
        """
        floor和ceil操作
        :param current_node:
        :param key:
        :param floor: 给定一个key，寻找比key小，但在所有比key小的元素中的最大值
        :param ceil: 给定一个key，寻找比key大，但在所有比key大的元素中的最小值
        :return:
        """
        if current_node:
            if current_node.key == key:
                floor, ceil = key, key
                return floor, ceil
            elif current_node.key < key:
                floor = current_node.key
                return self._get_floor_and_ceil(key, current_node.right_child, floor, ceil)
            else:
                ceil = current_node.key
                return self._get_floor_and_ceil(key, current_node.left_child, floor, ceil)

        else:
            return floor, ceil

    def pre_order(self):
        """
        前序遍历
        :return:
        """
        self._pre_order(self.root)

    def _pre_order(self, tree_node):
        print(tree_node.key)
        self._pre_order(tree_node.left_child)
        self._pre_order(tree_node.right_child)

    def in_order(self):
        """
        中序遍历
        :return:
        """
        self._in_order(self.root)

    def _in_order(self, tree_node):
        self._in_order(tree_node.left_child)
        print(tree_node.key)
        self._in_order(tree_node.right_child)

    def post_order(self):
        """
        后序遍历
        :return:
        """
        self._post_order(self.root)

    def _post_order(self, tree_node):
        self._post_order(tree_node.left_child)
        self._post_order(tree_node.right_child)
        print(tree_node.key)

    def level_order(self):
        """
        层序遍历
        :return:
        """
        q = queue.Queue()
        q.put(self.root)
        while q.not_empty():
            tree_node = q.get()
            print(tree_node.key)
            if tree_node.left_child:
                q.put(tree_node.left_child)
            if tree_node.right_child:
                q.put(tree_node.right_child)

    def minimum(self):
        """
        最小值节点
        :return:
        """
        node = self.root
        while node.left_child:
            node = node.left_child
        return node.key

    def maximum(self):
        """
        最大值节点
        :return:
        """
        node = self.root
        while node.right_child:
            node = node.right_child
        return node.key
