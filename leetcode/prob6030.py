# coding:utf-8
from typing import List


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        res = []

        for i in range(len(queryIndices)):
            s = s[:queryIndices[i]] + queryCharacters[i] + s[queryIndices[i] + 1:]
            print(s)

            maxlen = 1
            curlen = 1
            curC = s[0]
            for i in range(1, len(s)):
                if curC == s[i]:
                    curlen += 1
                    maxlen = max(maxlen, curlen)
                else:
                    curC = s[i]
                    curlen = 1

            res.append(maxlen)

        return res


s = Solution()
print(s.longestRepeating(s="babacc", queryCharacters="bcb", queryIndices=[1, 3, 3]))
print(s.longestRepeating(s="abyzz", queryCharacters="aa", queryIndices=[2, 1]))
