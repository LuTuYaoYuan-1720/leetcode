# coding:utf-8
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next = self.nextGreater(nums2)
        dctNext = {nums2[i]: next[i] for i in range(len(nums2))}
        res = [dctNext[num] for num in nums1]

        return res

    def nextGreater(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            # 比当前元素小的元素都要出栈
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop()

            res[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i])

        return res
