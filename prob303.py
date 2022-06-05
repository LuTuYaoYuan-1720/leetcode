# coding:utf-8
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = []
        self.presum.append(0)
        for i in range(len(nums)):
            self.presum.append(self.presum[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right + 1] - self.presum[left]
