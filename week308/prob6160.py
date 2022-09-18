# coding:utf-8

"""
@Project: pythonlearn
@IDE    : PyCharm
@Author : Eason Chan
@Date   : 2022/8/28 14:13
"""
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        preSum = [nums[0], ]

        for i in range(1, len(nums)):
            preSum.append(preSum[-1] + nums[i])

        for q in queries:
            index = 0
            while index < len(preSum):
                if preSum[index] > q:
                    break
                index += 1
            res.append(index)

        return res
