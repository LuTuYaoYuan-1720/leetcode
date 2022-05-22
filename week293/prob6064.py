# coding:utf-8
from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        mx = 0
        all = [bottom - 1]
        all.extend(sorted(special))
        all.append(top + 1)

        for i in range(len(all) - 1):
            mx = max(mx, all[i + 1] - all[i] - 1)

        return mx
