# coding:utf-8
from typing import List
from collections import Counter
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0

        cnts = Counter(nums)

        for n in cnts.keys():
            if n + k in cnts.keys():
                res += cnts.get(n) * cnts.get(n + k)
            if n - k in cnts.keys():
                res += cnts.get(n) * cnts.get(n - k)

        return res // 2

