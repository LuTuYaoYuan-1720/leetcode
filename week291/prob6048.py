# coding:utf-8
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cnt = {}
        for i, card in enumerate(cards):
            if card not in cnt:
                cnt[card] = [i]
            else:
                cnt[card].append(i)
        mn = 1e5
        for value in cnt.values():
            for i in range(len(value) - 1):
                mn = min(mn, value[i + 1] - value[i])
        if mn != 1e5:
            return mn + 1
        return -1


s = Solution()
s.minimumCardPickup(cards=[3, 4, 2, 3, 4, 7])
