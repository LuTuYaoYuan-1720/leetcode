# coding:utf-8
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        sign = [i for i in range(len(s)) if s[i] == c]

        for i in range(len(s)):

            if s[i] == c:
                res.append(0)
            else:
                if i < sign[0]:
                    res.append(sign[0] - i)
                elif i > sign[len(sign) - 1]:
                    res.append(i - sign[len(sign) - 1])
                else:
                    l, r = 0, 0
                    for j in range(len(sign) - 1):
                        if sign[j] < i < sign[j + 1]:
                            l = sign[j]
                            r = sign[j + 1]
                            break
                    res.append(min(i - l, r - i))

        return res
