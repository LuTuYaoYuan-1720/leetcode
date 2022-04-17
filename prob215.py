# coding:utf-8
from typing import List
from heapq import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq = []
        for num in nums:
            heappush(heapq, num)

        res = nlargest(k, heapq)[-1]
        return res
