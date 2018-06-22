# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/5/23 下午2:44'

给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。


题目的要求是输出Unix下的最简路径，Unix文件的根目录为"/"，"."表示当前目录，".."表示上级目录。

例如：

输入1：

/../a/b/c/./..

输出1：

/a/b

模拟整个过程：

1. "/" 根目录

2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"

3. "a" 进入子目录a，目前处于 "/a"

4. "b" 进入子目录b，目前处于 "/a/b"

5. "c" 进入子目录c，目前处于 "/a/b/c"

6. "." 当前目录，不操作，仍处于 "/a/b/c"

7. ".." 返回上级目录，最终为 "/a/b"

使用一个栈来解决问题。遇到'..'弹栈，遇到'.'不操作，其他情况下压栈。
"""


class Solution:
    # def simplifyPath(self, path):
    #     """
    #     :type path: str
    #     :rtype: str
    #     """
    #     stack = []
    #     i = 0
    #     res = ''
    #     while i < len(path):
    #         end = i + 1
    #         while end < len(path) and path[end] != '/':
    #             end += 1
    #         sub = path[i + 1:end]
    #         if len(sub) > 0:
    #             if sub == '..':
    #                 if stack:
    #                     stack.pop()
    #             elif sub != '.':
    #                 stack.append(sub)
    #         i = end
    #     if not stack:
    #         return '/'
    #     for i in stack:
    #         res += '/' + i
    #     return res

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        curr = '/'
        for i in path:
            if i == '..':
                if curr != '/':
                    curr = '/'.join(curr.split('/')[:-1])
                    if curr == '': curr = '/'
            elif i != '.' and i != '':
                curr += '/' + i if curr != '/' else i
        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath('/../a/b/c/./..'))
