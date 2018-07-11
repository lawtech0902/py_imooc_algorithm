# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/7/2 下午12:22'

TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，
它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。
你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
"""

import string
import random

full_tiny = {}
tiny_full = {}
letters = string.ascii_letters + string.digits


class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        def suffix():
            res, tmp = '', ''
            for _ in range(6):
                tmp = letters[random.randint(0, 10000) % 62]
                res += tmp
            return res

        if longUrl in full_tiny:
            return 'http://tinyurl.com/' + full_tiny[longUrl]
        else:
            suff = suffix()
            full_tiny[longUrl] = suff
            tiny_full[suff] = longUrl
            return "http://tinyurl.com/" + suff

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        suff = shortUrl.split('/')[-1]
        if suff in tiny_full:
            return tiny_full[suff]
        else:
            return None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
