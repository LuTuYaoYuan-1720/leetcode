# coding:utf-8
from typing import List

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        cnt = Counter(p)

        tmp = Counter(s[:len(p)])

        if tmp == cnt:
            res.append(0)

        for i in range(0, len(s) - len(p)):
            if tmp[s[i]] == 1:
                tmp.pop(s[i])
            else:
                tmp[s[i]] -= 1

            if s[i + len(p)] in tmp.keys():
                tmp[s[i + len(p)]] += 1
            else:
                tmp[s[i + len(p)]] = 1

            if tmp == cnt:
                res.append(i + 1)

        return res


s = Solution()
print(s.findAnagrams(s="cbaebabacd", p="abc"))
print(s.findAnagrams(s="abab", p="ab"))
