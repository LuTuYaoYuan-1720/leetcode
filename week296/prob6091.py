# coding:utf-8
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        left, right = 0, 0
        while right < len(nums):
            if nums[right] - nums[left] <= k:
                right += 1
                continue
            else:
                res += 1
                left = right
            right += 1

        return res + 1
