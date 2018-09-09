# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/9/2 下午10:56'
"""

import random
import string

full_to_tiny = {}
tiny_to_full = {}
letters = string.ascii_letters + string.digits


class Codec:

    def encode(self, long_url):
        def suffix():
            res, tmp = '', ''
            for _ in range(6):
                tmp = letters[random.randint(0, 10000) % 62]
                res += tmp
            return res

        if long_url in full_to_tiny:
            return 'http://tinyurl.com/' + full_to_tiny[long_url]
        else:
            suff = suffix()
            full_to_tiny[long_url] = suff
            tiny_to_full[suff] = long_url
            return 'http://tinyurl.com/' + suff

    def decode(self, tiny_url):
        suff = tiny_url.split('/')[-1]
        if suff in tiny_to_full:
            return tiny_to_full[suff]
        else:
            return None


if __name__ == '__main__':
    codec = Codec()
    encode = codec.encode('https://leetcode.com/problems/design-tinyurl')
    decode = codec.decode(encode)
    print(encode)
    print(decode)
