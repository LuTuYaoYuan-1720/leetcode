# coding:utf-8
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tmp = list({i[1] for i in trust})

        for t in tmp:
            p = []
            sign = True
            for i in trust:
                if i[1] == t:
                    p.append(i[0])
                if i[0] == t:
                    sign = False
                    break

            if len(p) == n - 1 and sign:
                return t

        return -1


s = Solution()
print(s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
