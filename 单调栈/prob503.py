# coding:utf-8
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        stack = []
        # 利用循环数组， 相当于将 nums 变成 [nums, nums]
        for i in range(2 * len(nums) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i % len(nums)]:
                stack.pop()

            res[i % len(nums)] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i % len(nums)])

        return res


s = Solution()
s.nextGreaterElements([2, 1, 2, 4, 3])
