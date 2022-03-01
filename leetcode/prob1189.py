# coding:utf-8
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnts = Counter(text)

        if 'a' in cnts.keys() and 'b' in cnts.keys() and 'l' in cnts.keys() and 'o' in cnts.keys() and 'n' in cnts.keys():
            return min(cnts.get('a'), cnts.get('b'), cnts.get('l') // 2, cnts.get('o') // 2, cnts.get('n'))
        else:
            return 0


