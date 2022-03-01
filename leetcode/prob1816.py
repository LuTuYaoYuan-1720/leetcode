# coding:utf-8
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s + ' '
        loc = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == ' ':
                cnt += 1
            if cnt == k:
                loc = i
                break

        return s[:loc]