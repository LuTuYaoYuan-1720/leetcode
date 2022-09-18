# coding:utf-8
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        need, window = Counter(p), {}
        valid = 0
        left, right = 0, 0
        while right < len(s):
            cur = s[right]
            right += 1
            if cur in need:
                if cur in window:
                    window[cur] += 1
                else:
                    window[cur] = 1
                if window[cur] == need[cur]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                cur = s[left]
                left += 1
                if cur in need:
                    if need[cur] == window[cur]:
                        valid -= 1
                    window[cur] -= 1

        return res
