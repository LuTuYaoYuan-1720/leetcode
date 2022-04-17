# coding:utf-8
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        if 2 * k + 1 > len(nums):
            return [-1] * len(nums)

        res = []

        for i in range(k):
            res.append(-1)

        n = len(nums) - 2 * k

        sum = 0

        for i in range(2 * k + 1):
            sum += nums[i]
        res.append(sum // (2 * k + 1))

        for i in range(n - 1):
            sum -= nums[i]
            sum += nums[i + 2 * k + 1]
            res.append(sum // (2 * k + 1))

        for i in range(k):
            res.append(-1)

        return res
