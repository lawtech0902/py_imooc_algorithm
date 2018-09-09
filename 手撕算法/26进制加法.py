# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/9 下午3:35'

百词斩/华为 笔试
"""

s1 = input()
s2 = input()

size1, size2 = len(s1), len(s2)
s1, s2 = s1[::-1], s2[::-1]

if size1 > size2:
    for i in range(size1 - size2):
        s2 += 'a'
    size2 = size1
else:
    for i in range(size2 - size1):
        s1 += 'a'
    size1 = size2

re = 0
c = ''

for i in range(size1):
    tmp = ord(s1[i]) - ord('a') + ord(s2[i]) - ord('a') + re
    if tmp // 26:
        re = 1
        c += chr(ord('a') + tmp % 26)
    else:
        re = 0
        c += chr(tmp + ord('a'))

if re:
    c += 'b'

print(c[::-1])
