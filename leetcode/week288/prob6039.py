# coding:utf-8
from typing import List
import heapq


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        res = 1
        heapq.heapify(nums)
        for i in range(k):
            tmp = heapq.heappop(nums)
            heapq.heappush(nums, tmp + 1)

        for num in nums:
            res *= num
            res %= int(1e9 + 7)

        return res


print(1e2)
