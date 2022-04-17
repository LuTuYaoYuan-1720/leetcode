# coding:utf-8

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res = ''

        cnt = 0
        tmp = 0

        while len(s) > k:
            for i in range(len(s)):
                tmp += int(s[i])
                cnt += 1
                if cnt == k or i == len(s) - 1:
                    res += str(tmp)
                    cnt = 0
                    tmp = 0
            s = res
            res = ''

        return s
