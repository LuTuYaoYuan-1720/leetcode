# coding:utf-8
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        lenRes = len(nums)
        idx = 0
        while lenRes != 1:
            sign = True
            for i in range(lenRes // 2):
                if sign:
                    nums[idx] = min(nums[2 * i], nums[2 * i + 1])
                    sign = False
                else:
                    nums[idx] = max(nums[2 * i], nums[2 * i + 1])
                    sign = True
                idx += 1
            idx = 0
            lenRes //= 2

        return nums[0]
