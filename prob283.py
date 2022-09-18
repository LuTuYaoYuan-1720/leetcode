# coding:utf-8
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        for i in range(slow, len(nums)):
            nums[i] = 0
