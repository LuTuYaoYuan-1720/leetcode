# coding:utf-8
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = len(prices)
        down = []
        cur_len = 1
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] == -1:
                cur_len += 1
            else:
                if cur_len != 1:
                    down.append(cur_len)
                    cur_len = 1
        if cur_len != 1:
            down.append(cur_len)

        for i in down:
            res += (i - 1) * (1 + i - 1) // 2
        return res


s = Solution()
s.getDescentPeriods([3, 2, 1, 4])
print(s.getDescentPeriods([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 3, 10, 9, 8, 7]))
