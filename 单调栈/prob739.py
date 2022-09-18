# coding:utf-8
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            # prob496问的是紧跟着的一个数，这个题问的是紧跟着的 idx 和当前差了几位
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            res[i] = 0 if len(stack) == 0 else stack[-1] - i
            stack.append(i)

        return res


s = Solution()
s.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
