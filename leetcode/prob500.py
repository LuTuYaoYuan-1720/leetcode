# coding:utf-8
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []

        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"

        for word in words:
            chars = list(word.lower())
            if self.wordIn(chars, first) or self.wordIn(chars, second) or self.wordIn(chars, third):
                res.append(word)

        return res

    def wordIn(self, chars: List[str], row: str) -> bool:
        res = True

        for c in chars:
            if c not in row:
                res = False
                break

        return res
