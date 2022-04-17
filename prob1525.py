# coding:utf-8

from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        pre = s[0]
        suff = s[1:]
        pre_cnt = Counter(pre)
        suff_cnt = Counter(suff)

        for i in range(1, len(s)):
            if len(pre_cnt.keys()) == len(suff_cnt.keys()):
                res += 1

            if s[i] in pre_cnt.keys():
                pre_cnt[s[i]] += 1
            else:
                pre_cnt[s[i]] = 1

            if suff_cnt[s[i]] == 1:
                suff_cnt.pop(s[i])
            else:
                suff_cnt[s[i]] -= 1

        return res


s = Solution()
print(s.numSplits("aabbaa"))
