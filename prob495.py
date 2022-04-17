# coding:utf-8
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = set()

        for i in timeSeries:
            for num in range(i, i + duration):
                res.add(num)

        return len(res)
