# coding:utf-8
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = 1440

        times = []
        for time in timePoints:
            times.append(int(time[:2]) * 60 + int(time[3:]))

        times = sorted(times)

        for i in range(1, len(times)):
            res = min(res, times[i] - times[i - 1], 1440 - (times[i] - times[i - 1]))

        return min(res, times[-1] - times[0], 1440 - (times[-1] - times[0]))
