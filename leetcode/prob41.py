# coding:utf-8
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        sign = {}
        for num in nums:
            if num > 0:
                sign[num] = 1

        i = 1
        while i < 2 ** 31:
            if i not in sign:
                return i
            else:
                i += 1

        return 0
