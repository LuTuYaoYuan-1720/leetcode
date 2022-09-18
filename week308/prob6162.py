# coding:utf-8

"""
@Project: pythonlearn
@IDE    : PyCharm
@Author : Eason Chan
@Date   : 2022/8/28 10:55
"""
from typing import List
from collections import Counter


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        contain = [[], [], []]

        for i in range(len(garbage)):
            cnt = Counter(garbage[i])
            res += len(garbage[i])
            if cnt.get('M') is not None:
                contain[0].append(i)
            if cnt.get('P') is not None:
                contain[1].append(i)
            if cnt.get('G') is not None:
                contain[2].append(i)

        if len(contain[0]) != 0:
            res += sum(travel[:contain[0][-1]])

        if len(contain[1]) != 0:
            res += sum(travel[:contain[1][-1]])

        if len(contain[2]) != 0:
            res += sum(travel[:contain[2][-1]])

        return res
