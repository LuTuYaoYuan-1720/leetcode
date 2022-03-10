# coding:utf-8
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []

        col1 = s[0]
        col2 = s[3]
        row1 = s[1]
        row2 = s[4]

        for i in range(ord(col1), ord(col2) + 1):
            for j in range(int(row1), int(row2) + 1):
                res.append(chr(i) + str(j))

        return res

