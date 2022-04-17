# coding:utf-8
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        s = s + ' '
        res = 0
        tmp = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == tmp:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
                tmp = s[i]

        return res


s = Solution()
s.maxPower(s="leetcode")
s.maxPower(s="abbcccddddeeeeedcba")
s.maxPower(s="hooraaaaaaaaaaay")
