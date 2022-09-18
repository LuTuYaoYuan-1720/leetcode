# coding:utf-8

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            single = self.search(s, i, i)
            double = self.search(s, i, i + 1)
            res = single if len(single) > len(res) else res
            res = double if len(double) > len(res) else res
        return res

    def search(self, s: str, l: int, r: int):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l + 1: r]
