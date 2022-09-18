# coding:utf-8

"""
@Project: pythonlearn
@IDE    : PyCharm
@Author : Eason Chan
@Date   : 2022/9/4 10:33
"""
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dct = {}
        for i in range(len(s)):
            if not dct.get(s[i]):
                dct[s[i]] = [i]
            else:
                dct[s[i]].append(i)

        for k, v in dct.items():
            dis = distance[ord(k) - 97]
            if v[1] - v[0] - 1 != dis:
                return False
        return True
