# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/6 下午4:13'
"""


def right_strip(tmp_str, split_str=' '):
    end_ind = tmp_str.rfind(split_str)
    while end_ind != -1 and end_ind == len(tmp_str) - 1:
        tmp_str = tmp_str[:end_ind]
        end_ind = tmp_str.rfind(split_str)
    return tmp_str


def left_strip(tmp_str, split_str=' '):
    start_ind = tmp_str.find(split_str)
    while start_ind == 0:
        tmp_str = tmp_str[start_ind + 1:]
        start_ind = tmp_str.find(split_str)
    return tmp_str
