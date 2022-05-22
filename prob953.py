# coding:utf-8
from typing import List


class Solution:
    """
    先将词典序存起来
    然后拿出分别拿出两个看是否按照词典序排列
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct = {}
        for i in range(1, 27):
            dct[order[i - 1]] = i
        dct[' '] = 0

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            if len(w1) < len(w2):
                w1 = w1 + ' ' * (len(w2) - len(w1))
            else:
                w2 = w2 + ' ' * (len(w1) - len(w2))

            for idx in range(len(w1)):
                if dct[w1[idx]] > dct[w2[idx]]:
                    return False
                elif dct[w1[idx]] < dct[w2[idx]]:
                    break
                else:
                    continue

        return True


s = Solution()
s.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
