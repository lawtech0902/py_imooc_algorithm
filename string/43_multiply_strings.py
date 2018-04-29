# _*_ coding: utf-8 _*_
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
大数乘法
算法的关键是要先将两个字符串翻转过来，
然后按位进行相乘，相乘后的数不要着急进位，而是存储在一个数组里面，
然后将数组中的数对10进行求余（%），就是这一位的数，然后除以10，即/10，就是进位的数。
注意最后要将相乘后的字符串前面的0去掉。
__author__ = 'lawtech'
__date__ = '2018/4/28 下午3:41'
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        arr = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i + j] += int(num1[i]) * int(num2[j])
        res = []
        for i in range(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] // 10
            if i < len(arr) - 1:
                arr[i + 1] += carry
            res.insert(0, str(digit))
        while res[0] == '0' and len(res) > 1:
            del res[0]
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('123', '456'))
