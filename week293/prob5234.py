# coding:utf-8
from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            cur = Counter(words[i])
            if cur == Counter(words[i - 1]):
                del words[i]
            else:
                i += 1

        return words
