# coding:utf-8
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        # {person: [wincnt, loscnt]}
        cnt = {}
        for match in matches:
            if match[0] in cnt.keys():
                cnt[match[0]][0] += 1
            else:
                cnt[match[0]] = [1, 0]

            if match[1] in cnt.keys():
                cnt[match[1]][1] += 1
            else:
                cnt[match[1]] = [0, 1]

        for key, value in cnt.items():
            if value[0] >= 1 and value[1] == 0:
                res[0].append(key)
            if value[1] == 1:
                res[1].append(key)
        res[0].sort()
        res[1].sort()
        return res
