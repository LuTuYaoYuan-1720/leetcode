# coding:utf-8
from typing import List
from numpy import *


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        res = set()
        res.add(0)
        res.add(firstPerson)
        a = array(meetings)
        a = a[a[:, 2].argsort()]
        print(a)

        return list(res)
