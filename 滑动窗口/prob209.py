# coding:utf-8
from typing import List
import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = sys.maxsize
        left, right = 0, 0
        curSum = 0

        while right < len(nums):
            cur = nums[right]
            right += 1
            curSum += cur

            while curSum >= target:
                res = min(res, right - left)
                cur = nums[left]
                left += 1
                curSum -= cur

        return 0 if res == sys.maxsize else res
