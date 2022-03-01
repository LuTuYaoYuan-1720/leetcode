# coding:utf-8
from typing import List
from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        person_every_time = []
        m = 0
        votes = defaultdict(int)
        tmp_person = -1
        for v in persons:
            votes[v] += 1
            if votes[v] >= m:
                m = votes[v]
                tmp_person = v
            person_every_time.append(tmp_person)

        self.times = times
        self.person_every_time = person_every_time

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        # 找到满足 times[l] <= t 的最大的 l
        while l < r:
            m = l + (r - l + 1) // 2
            if self.times[m] <= t:
                l = m
            else:
                r = m - 1
        # 也可以使用内置的二分查找的包来确定 l
        # l = bisect.bisect(self.times, t) - 1
        return self.person_every_time[l]


s = TopVotedCandidate([0, 0, 1, 1, 2], [0, 67, 69, 74, 87])
arr = [4, 62, 100, 88, 70, 73, 22, 75, 29, 10]
for n in arr:
    s.q(n)
