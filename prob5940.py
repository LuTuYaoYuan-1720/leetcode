# coding:utf-8
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = -1
        max_index = -1
        min_num = 10000000
        max_num = -10000000

        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i

            if nums[i] < min_num:
                min_num = nums[i]
                min_index = i

        l = min(min_index, max_index)
        r = max(min_index, max_index)

        res = min(len(nums) - r + l + 1, r + 1, len(nums) - l)

        return res
