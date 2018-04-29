# _*_ coding: utf-8 _*_
"""
KMP python 实现
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html

重点：生成部分匹配表，然后匹配
移动位数 = 已匹配字符数 - 对应的部分匹配值

部分匹配值：前缀和后缀的最长的共有元素的长度
__author__ = 'lawtech'
__date__ = '2018/3/19 下午6:46'
"""


def kmp_match(s, p):
    m, n = len(s), len(p)
    cur = 0  # 起始指针
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        else:
            return True
    return False


def partial_table(p):
    """
    partial_table("ABCDABD") -> [0,0,0,0,1,2,0]
    """
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret


if __name__ == '__main__':
    s = "BBC ABCDAB ABCDABCDABDE"
    p = "ABCDEABC"
    print(partial_table(p))
