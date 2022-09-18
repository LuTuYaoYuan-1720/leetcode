# coding:utf-8
from typing import List

from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res0 = 0
        for k, v in cnt.items():
            res0 += v // 2

        return [res0, len(nums) - res0 * 2]
