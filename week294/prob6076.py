# coding:utf-8
from math import gcd
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        # 用最大公因子
        stockPrices.sort()
        pre = None
        ans = 0
        for i in range(1, len(stockPrices)):
            a = stockPrices[i][0] - stockPrices[i - 1][0]
            b = stockPrices[i][1] - stockPrices[i - 1][1]
            g = gcd(a, b)
            k = [a // g, b // g]
            if pre is None or k != pre:
                ans += 1
            pre = k
        return ans

        # 77 / 79 浮点数精度问题
        # res = 1
        # stockPrices.sort(key=lambda x: x[0])
        # xie = []
        # for i in range(len(stockPrices) - 1):
        #     xie.append((stockPrices[i + 1][1] - stockPrices[i][1]) / (stockPrices[i + 1][0] - stockPrices[i][0]))
        # cur = xie[0]
        # for i in range(1, len(xie)):
        #     if xie[i] == cur:
        #         continue
        #     else:
        #         res += 1
        #         cur = xie[i]
        #
        # return res


s = Solution()
s.minimumLines([[3, 4], [1, 2], [7, 8], [2, 3]])
s.minimumLines([[1, 1], [500000000, 499999999], [1000000000, 999999998]])
