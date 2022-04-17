# coding:utf-8
from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        if 1 in cnt.values():
            return -1
        res = 0
        for num in cnt.values():
            if num % 3 == 1:
                res += (num - 3) // 3 + 2
            elif num % 3 == 2:
                res += num // 3 + 1
            else:
                res += num // 3

        return res
