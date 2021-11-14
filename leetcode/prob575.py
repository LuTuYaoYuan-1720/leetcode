# coding:utf-8
from typing import List

from collections import Counter


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        cnts = Counter(candyType)

        if len(cnts) >= len(candyType) // 2:
            return len(candyType) // 2
        else:
            return len(cnts)
