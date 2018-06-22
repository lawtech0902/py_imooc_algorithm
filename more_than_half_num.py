# -*- coding:utf-8 -*-
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         from collections import Counter
#         cnt = Counter(numbers)
#         max_cnt = max(cnt.keys())
#         flag = max(cnt) > (len(numbers) // 2)
#         return sorted(cnt.items(), key=lambda item: item[1])[-1][0] if flag else 0


# if __name__ == '__main__':
#     nums = [1, 2, 3, 2, 4, 2, 5, 2, 3]
#     s = Solution()
#     print(s.MoreThanHalfNum_Solution(nums))


class Solution:
    def MoreThanHalfNum_Solution(self, nums):
        # write code here
        if not nums:
            return 0
        candidate, cnt = None, 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt += 1
            elif num == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate


if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
