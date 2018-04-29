# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        from collections import Counter
        cnt = Counter(numbers)
        max_cnt = max(cnt.keys())
        flag = max(cnt) > (len(numbers) // 2)
        return sorted(cnt.items(), key=lambda item: item[1])[-1][0] if flag else 0


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(nums))
