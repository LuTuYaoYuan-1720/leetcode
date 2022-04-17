# coding:utf-8
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []

        for i in range(2, n + 1):
            for j in range(1, i):
                yueshu = self.f(i, j)
                if yueshu != 1:
                    s = str(j // yueshu) + '/' + str(i // yueshu)
                    if s not in res:
                        res.append(s)
                else:
                    s = str(j) + '/' + str(i)

                if s not in res:
                    res.append(s)

        return res

    def f(self, x: int, y: int):
        z = y
        while x % y != 0:
            z = x % y
            x = y
            y = z

        return z
