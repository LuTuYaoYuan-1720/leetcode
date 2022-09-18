# coding:utf-8
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            tmp = self.f(num)
            if tmp in dct:
                dct[tmp].append(num)
            else:
                dct[tmp] = [num]

        res = -1
        for l in dct.values():
            if len(l) < 2:
                continue
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    res = max(res, l[i] + l[j])

        return res

    def f(self, num):
        res = 0
        while num != 0:
            res += num % 10
            num //= 10
        return res
