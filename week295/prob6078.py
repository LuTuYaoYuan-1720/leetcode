# coding:utf-8

from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tgtCnt = Counter(target)
        sCnt = Counter(s)
        res = 100
        for k, v in tgtCnt.items():
            res = min(res, sCnt[k] // v)

        return res


s = Solution()
s.rearrangeCharacters(s="ilovecodingonleetcode", target="code")
