# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/6/19 下午3:21'

题目太特么长了！
"""


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        bc = -1
        for num, line in enumerate(source):
            content = ''
            shrink = False
            while True:
                if bc >= 0:
                    shrink = (bc != num)
                    end = line.find('*/')
                    if end == -1:
                        break
                    line = line[end+2:]
                    bc = -1
                lstart = line.find('//')
                bstart = line.find('/*')
                if lstart >= 0 and (bstart > lstart or bstart < 0):
                    content += line[:lstart]
                    break
                elif bstart >= 0:
                    content += line[:bstart]
                    line = line[bstart+2:]
                    bc = num
                else:
                    content += line
                    break
            if shrink:
                content = result.pop() + content
            if content:
                result.append(content)
        return result
