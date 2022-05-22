# coding:utf-8
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        nums = [capacity[i] - rocks[i] for i in range(len(capacity))]
        nums.sort()
        for num in nums:
            if additionalRocks - num >= 0:
                res += 1
                additionalRocks -= num
            else:
                break

        return res
