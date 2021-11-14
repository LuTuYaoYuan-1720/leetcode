# coding:utf-8
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnts = Counter(nums)

        res = [k for k, v in cnts.items() if v == 1]

        return res


s = Solution()
print(s.singleNumber(nums=[1, 2, 1, 3, 2, 5]))
