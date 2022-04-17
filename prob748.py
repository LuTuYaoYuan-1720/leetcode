# coding:utf-8
from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res = '1111111111111111111'
        min_len = len(res)
        res_arr = []
        l = ''
        for c in licensePlate:
            if c.isalpha():
                l += c.lower()

        print(l)
        l_cnt = Counter(l)
        for word in words:
            if len(word) <= len(res):
                word_cnt = Counter(word)
                sign = True
                for k in l_cnt:
                    if k in word_cnt.keys() and word_cnt.get(k) >= l_cnt.get(k):
                        continue
                    else:
                        sign = False
                        break
                if sign:
                    min_len = min(min_len, len(word))
                    res_arr.append(word)
        for r in res_arr:
            if len(r) == min_len:
                return r
