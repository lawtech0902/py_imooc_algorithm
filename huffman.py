# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/4/17 下午2:57'
"""
from collections import Counter


class Node(object):
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq  # 出现频率

    def is_left(self):
        return self.father == self


def count_freq(text):
    chars = []
    chars_freqs = []
    for i in range(0, len(text)):
        if text[i] in chars:
            pass
        else:
            chars.append(text[i])
            char_freq = (text[i], text.count(text[i]))
            chars_freqs.append(char_freq)
    return chars_freqs


def create_nodes(freqs):
    return [Node(freq) for freq in freqs]


def huffman_tree(nodes):
    # 建树
    q = nodes[:]
    while len(q) > 1:
        q.sort(key=lambda char: char.freq)
        left = q.pop(0)
        right = q.pop(0)
        father = Node(left.freq + right.freq)
        father.left = left
        father.right = right
        left.father = father
        right.father = father
        q.append(father)
    q[0].father = None
    return q[0]


def huffman_encode(nodes, root):
    # 编码每个字符, 自底向上
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.is_left():
                codes[i] += '0'
            else:
                codes[i] += '1'
            node_tmp = node_tmp.father
    return codes


def encode_str(s, freqs, codes):
    huffmanStr = ''
    for char in s:
        i = 0
        for item in freqs:
            if char == item[0]:
                huffmanStr += codes[i]
            i += 1
    return huffmanStr


if __name__ == '__main__':
    s = 'lejvRfDaMZPMWZRfGovHBWYolWnCezImtQcFMwoBCMTOoDaJqkoXPAfLBKjkFNtEoBwqqtaCKahiffRywjvNmOXrNpHlVfGfpNFwEPilghSdWFwfZONjOYZzZSYxZFPCJGYEVSybqQpohdXykkSrRYrorfaxQwXtdgCGLyEEwaKHhFTLfrdzQodVECpHjLJZEznuldpTsLweysTMGVOaNjbgmoaexPstHeCpGaOiXExcJoPIiBlYwCXzIvSWIkAZBNZiVqYaRBoUDnjxdASdqmmuueJvmOBZCWyyEtxhhsULBcGVJxqJcZjezpkcqGGzSIxjcQFIowkZQkVhmtchdWzbhNVyooeiyjHxgwszYxPuzCxBioLFvSkLpzyLxnHAlWcOFJVTlIihFdDlKKQedMFcPxalZNcnLxBCTZmBIMHVXzMuzzinnwOKMxqHiZAaOpFnnsYJSiZtLqUgFfmyAfarEqkrYoaEIgoAkxRKhhIRtAMzOcLvrFNPLWzoWejYAeqKPvqSiLImVlHrXJtBBlJhrEkkLytbDVTZPXQKEIqRjvVEsYgNOaYgNNObSFAZSzuTWPhloambZdOPRtYjdRvTTZkHMBuEBgxBgqtgXyjVyBcRGrvKjDBDncOistGVbCUyOOzJYZXOIzVxuFOXGYlNmoCNLBxvmxHawqWpWrRFxPglNTzHbcCrZuDlELssLXyFOwCiObVYRCxtNwGigISuACCfMlPVMEmBmqvTUAkqVHPwhmWcQOhBbYJLKoUNBAXfMXIBbDPgRYsEPAEytKNyOwaANQqHSdSwSlunEThLsuGBFWJFjRaOuPYiLXmpgObEPUUYmJzTrgqzbkJpTnxIdRdLOxKLrdxGPbhtaOJARhndRJqKKrDbNuLnLKfcexbHyTBItEgDGEGrBsKdysaeySgabCUBFrRAzQhzMqXurdlOBOYOFXvfSMQCYiLRoiPgHpZG'
    freqs = count_freq(s)
    nodes = create_nodes([item[1] for item in freqs])
    root = huffman_tree(nodes)
    codes = huffman_encode(nodes, root)
    huffman_str = encode_str(s, freqs, codes)
    print(len(huffman_str))
