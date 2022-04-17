# coding:utf-8
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        cnts = Counter(nums)

        for k in cnts.keys():
            if k - 1 in cnts.keys():
                res = max(cnts.get(k - 1) + cnts.get(k), res)
            if k + 1 in cnts.keys():
                res = max(cnts.get(k + 1) + cnts.get(k), res)

        return res


s = Solution()
print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
