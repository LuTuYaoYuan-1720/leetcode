# coding:utf-8
from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        paragraph = paragraph + " "
        sign = False
        for i in range(len(paragraph)):
            if sign is False:
                if paragraph[i].isalpha():
                    start = i
                    sign = True
                continue

            if paragraph[i].isalpha():
                continue
            else:
                words.append(paragraph[start:i].lower())
                sign = False
        cnt = Counter(words)
        for key in cnt.most_common():
            if key not in banned:
                return key
