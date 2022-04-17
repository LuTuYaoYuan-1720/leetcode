# coding:utf-8
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        word = [s[0:spaces[0]]]
        for i in range(len(spaces) - 1):
            word.append(s[spaces[i]:spaces[i + 1]])

        word.append(s[spaces[-1]:])
        return ' '.join(word)


s = Solution()
print(s.addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9]))
