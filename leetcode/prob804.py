# coding:utf-8
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        moss = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        dct = {}
        for i in range(26):
            chr(i + 97)
            dct[chr(i + 97)] = moss[i]
        res = set()
        for word in words:
            tmp = ''
            for c in word:
                tmp += dct[c]
            res.add(tmp)
        return len(res)


s = Solution()
s.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
