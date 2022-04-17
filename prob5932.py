# coding:utf-8
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        res = []
        n = 0

        for i in range(len(pairs)):
            res = [pairs[i]]
            for item in pairs:
                if item[0] == res[n][1]:
                    res.append(item)
                    n += 1
            if len(res) == len(pairs):
                return res
            else:
                n = 0
                res = [pairs[i]]

        return res


s = Solution()
print(s.validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]))
