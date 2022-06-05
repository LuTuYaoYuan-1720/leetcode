# coding:utf-8
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
            dct[num] = i

        for op in operations:
            nums[dct[op[0]]] = op[1]
            dct[op[1]] = dct[op[0]]
            dct.pop(op[0])

        return nums
